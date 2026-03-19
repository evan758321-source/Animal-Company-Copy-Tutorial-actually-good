from flask import Flask, request, jsonify, send_file
import requests, json, ipaddress, secrets, base64, time, sqlite3, random, os, string

GENERATE_FRESH_TOKENS = True
DB_PATH = '/home/XeraCompany/mysite/userdata.db'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            ip TEXT PRIMARY KEY,
            username TEXT NOT NULL,
            custom_id TEXT NOT NULL,
            create_time REAL NOT NULL
        )
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS banned_ips (
            ip TEXT PRIMARY KEY
        )
    ''')
    conn.commit()
    conn.close()

app = Flask(__name__)
init_db()

DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/YOUR_WEBHOOK_HERE'

@app.after_request
def log_request(response):
    method = request.method
    url = request.url
    path = request.path
    headers = dict(request.headers)
    body = request.get_data(as_text=True)
    query_params = dict(request.args)
    status_code = response.status_code

    message = {
        'content': f"📡 **Request to: {path}**",
        'embeds': [{
            'title': 'Request Details',
            'fields': [
                {'name': 'Method', 'value': method, 'inline': True},
                {'name': 'Path', 'value': path, 'inline': True},
                {'name': 'Status Code', 'value': str(status_code), 'inline': True},
                {'name': 'Full URL', 'value': url, 'inline': False},
                {'name': 'Query Params', 'value': f"```json\n{json.dumps(query_params, indent=2)}```" if query_params else '*(none)*', 'inline': False},
                {'name': 'Headers', 'value': f"```json\n{json.dumps(headers, indent=2)}```", 'inline': False},
                {'name': 'Body', 'value': f"```json\n{body}```" if body else '*(empty)*', 'inline': False}
            ],
            'color': 65280 if status_code < 400 else 16711680
        }]
    }
    try:
        requests.post(DISCORD_WEBHOOK_URL, json=message)
    except Exception:
        pass
    return response


def generate_username():
    return 'Xera+' + ''.join(random.choices(string.ascii_uppercase, k=6))


def generate_gameplay_loadout():
    try:
        with open('/home/XeraCompany/mysite/econ_gameplay_items.json', 'r') as f:
            data = json.load(f)
        item_ids = [item['id'] for item in data if 'id' in item]
    except Exception as e:
        print(f"Failed to load econ_gameplay_items.json: {e}")
        item_ids = [
            'item_jetpack', 'item_flaregun', 'item_dynamite', 'item_tablet',
            'item_flashlight_mega', 'item_plunger', 'item_crossbow',
            'item_revolver', 'item_shotgun', 'item_pickaxe'
        ]

    children = []
    for _ in range(20):
        if random.random() < 0.7 and 'item_arena_pistol' in item_ids:
            selected_item = 'item_arena_pistol'
        else:
            selected_item = random.choice(item_ids)
        children.append({
            'itemID': selected_item,
            'scaleModifier': 100,
            'colorHue': random.randint(10, 111),
            'colorSaturation': random.randint(10, 111)
        })

    payload = {
        'objects': [{
            'collection': 'user_inventory',
            'key': 'gameplay_loadout',
            'permission_read': 1,
            'permission_write': 1,
            'value': json.dumps({
                'version': 1,
                'back': {
                    'itemID': 'item_backpack_large_base',
                    'scaleModifier': 120,
                    'colorHue': 50,
                    'colorSaturation': 50,
                    'children': children
                }
            })
        }]
    }
    return payload


def is_trusted_ip(ip_address):
    try:
        trusted_public_ips = {'YOUR_TRUSTED_IP_1', 'YOUR_TRUSTED_IP_2'}
        if ip_address in trusted_public_ips:
            return True
        ip = ipaddress.ip_address(ip_address)
        if ip.version == 4:
            return (
                ip in ipaddress.IPv4Network('YOUR_SUBNET_1/24') or
                ip in ipaddress.IPv4Network('YOUR_SUBNET_2/29')
            )
        return ip in ipaddress.IPv6Network('YOUR_IPV6_SUBNET/64')
    except ValueError:
        return False


def generate_custom_id():
    return ''.join(random.choices(string.digits, k=17))


def get_client_ip():
    return request.headers.get('X-Forwarded-For', request.remote_addr)


def get_or_create_user(ip):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute('SELECT 1 FROM banned_ips WHERE ip = ?', (ip,))
    if cur.fetchone():
        conn.close()
        return None, True

    cur.execute('SELECT username, custom_id FROM users WHERE ip = ?', (ip,))
    result = cur.fetchone()

    if result:
        username, custom_id = result
    else:
        if ip == '127.0.0.1':
            username = '<color=red>0x11'
        else:
            username = generate_username()
        custom_id = generate_custom_id()
        cur.execute(
            'INSERT INTO users (ip, username, custom_id, create_time) VALUES (?, ?, ?, ?)',
            (ip, username, custom_id, time.time())
        )
        conn.commit()

    conn.close()
    return {'username': username, 'custom_id': custom_id}, False


def generate_jwt(user_id):
    header = {'alg': 'HS256', 'typ': 'JWT'}
    now = int(time.time())
    payload = {
        'tid': secrets.token_hex(16),
        'uid': user_id,
        'usn': secrets.token_hex(5),
        'vrs': {
            'authID': secrets.token_hex(20),
            'clientUserAgent': 'MetaQuest 1.16.3.1138_5edcbd98',
            'deviceID': secrets.token_hex(20),
            'loginType': 'meta_quest'
        },
        'exp': now + 72000,
        'iat': now
    }

    def b64encode(obj):
        return base64.urlsafe_b64encode(json.dumps(obj).encode()).decode().rstrip('=')

    signature = secrets.token_urlsafe(32)
    return f"{b64encode(header)}.{b64encode(payload)}.{signature}"


def generate_token_pair():
    user_id = secrets.token_hex(16)
    return {
        'token': generate_jwt(user_id),
        'refresh_token': generate_jwt(user_id)
    }


STATIC_TOKEN_PAIR = {
    'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0aWQiOiI3OGU0NDBiOS00NWZjLTRhODYtOTllMy02ZGM5Y2RjN2M1N2UiLCJ1aWQiOiJmM2E1NjE4YS1hMzNmLTQyMDAtYThiYS1lYjM3YzdiZmJmOWMiLCJ1c24iOiJ4ZW5pdHl5dCIsInZycyI6eyJhdXRoSUQiOiJkYTEzZjU4YzJiMjU0ZTgwYTM5YzA3YzRlNzkyNjlmOSIsImNsaWVudFVzZXJBZ2VudCI6Ik1ldGFRdWVzdCAxLjE2LjMuMTEzOF81ZWRjYmQ5OCIsImRldmljZUlEIjoiMTcyZjZjMmU3MWE5NGMwMTBjMWY2Mjk5OWJjM2QzMjEiLCJsb2dpblR5cGUiOiJtZXRhX3F1ZXN0In0sImV4cCI6MTc0NDA2MzQwNiwiaWF0IjoxNzQzOTk0MzE4fQ.nRJLbep6nCGeBTwruOunyNjDUiLxfcvpAJHl7E6n3m8',
    'refresh_token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0aWQiOiI3OGU0NDBiOS00NWZjLTRhODYtOTllMy02ZGM5Y2RjN2M1N2UiLCJ1aWQiOiJmM2E1NjE4YS1hMzNmLTQyMDAtYThiYS1lYjM3YzdiZmJmOWMiLCJ1c24iOiJ4ZW5pdHl5dCIsInZycyI6eyJhdXRoSUQiOiJkYTEzZjU4YzJiMjU0ZTgwYTM5YzA3YzRlNzkyNjlmOSIsImNsaWVudFVzZXJBZ2VudCI6Ik1ldGFRdWVzdCAxLjE2LjMuMTEzOF81ZWRjYmQ5OCIsImRldmljZUlEIjoiMTcyZjZjMmU3MWE5NGMwMTBjMWY2Mjk5OWJjM2QzMjEiLCJsb2dpblR5cGUiOiJtZXRhX3F1ZXN0In0sImV4cCI6MTc0NDE0NjIwNiwiaWF0IjoxNzQzOTk0MzE4fQ.f7nTHNnPrJW6oYYo54RDks1iDvntTP2yiBfpHdH-ygQ'
}

CLIENT_BOOTSTRAP_RESPONSE = {
    'payload': '{"updateType":"Optional","attestResult":"Valid","attestTokenExpiresAt":1820877961,"photonAppID":"YOUR_PHOTON_APP_ID","photonVoiceAppID":"YOUR_PHOTON_VOICE_APP_ID","termsAcceptanceNeeded":[],"dailyMissionDateKey":"","dailyMissions":null,"dailyMissionResetTime":0,"serverTimeUnix":1720877961,"gameDataURL":"https://xeracompany.pythonanywhere.com/game-data-prod.zip"}'
}

ECON_ITEMS_RESPONSE = {
    'payload': '[{"id":"item_apple","netID":71,"name":"Apple","description":"An apple a day keeps the doctor away!","category":"Consumables","price":200,"value":7,"isLoot":true,"isPurchasable":false,"isUnique":false,"isDevOnly":false}, ...]'
}

SERVER_TIME_RESPONSE = {
    'payload': '{"serverTimeUnix":1720877961,"cachedExpiresAt":1820877961}'
}

STATIC_STORAGE_OBJECTS = {
    'objects': [
        {
            'collection': 'user_avatar',
            'key': '0',
            'user_id': '2e8aace0-282d-4c3d-b9d4-6a3b3ba2c2a6',
            'value': '{"butt":"bp_butt_gorilla","head":"bp_head_gorilla","tail":"","torso":"bp_torso_gorilla","armLeft":"bp_arm_l_gorilla","eyeLeft":"bp_eye_gorilla","armRight":"bp_arm_r_gorilla","eyeRight":"bp_eye_gorilla","accessories":["acc_fit_varsityjacket"],"primaryColor":"604170"}',
            'version': '7a326a2a4d0639a5f08e3116bb99a3bf',
            'permission_read': 2,
            'create_time': '2024-10-29T00:22:08Z',
            'update_time': '2025-04-04T03:55:19Z'
        },
        # ... other static objects remain the same
    ]
}

STATIC_ACCOUNT_RESPONSE = {
    'user': {
        'id': '2e8aace0-282d-4c3d-b9d4-6a3b3ba2c2a6',
        'username': 'ERROR',
        'lang_tag': 'en',
        'metadata': '{}',
        'edge_count': 4,
        'create_time': '2024-08-24T07:30:12Z',
        'update_time': '2025-04-05T21:00:27Z'
    },
    'wallet': '{"stashCols": 4, "stashRows": 2, "hardCurrency": 30000000, "softCurrency": 20000000, "researchPoints": 500000}',
    'custom_id': '26344644298513663'
}


# ─── Routes ───────────────────────────────────────────────────────────────────

@app.route('/v2/account/authenticate/custom', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
def authenticate_custom():
    generate_gameplay_loadout()
    return jsonify(generate_token_pair() if GENERATE_FRESH_TOKENS else STATIC_TOKEN_PAIR)


@app.route('/v2/account1', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
def account_alt():
    return jsonify(STATIC_ACCOUNT_RESPONSE)


@app.route('/v2/rpc/purchase.avatarItems', methods=['POST'])
def purchase_avatar_items():
    return jsonify({'payload': ''})


@app.route('/v2/rpc/avatar.update', methods=['POST'])
def avatar_update():
    return jsonify({'payload': ''})


@app.route('/v2/rpc/purchase.gameplayItems', methods=['POST'])
def purchase_gameplay_items():
    return jsonify({'payload': ''})


@app.route('/game-data-prod.zip')
def serve_game_data():
    client_ip = request.remote_addr
    print(f"Request from IP: {client_ip}")

    file_name = 'Zombie.zip'
    file_path = os.path.join('/home/XeraCompany/mysite', file_name)

    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return 'File not found', 404

    file_size = os.path.getsize(file_path)
    print(f"Serving {file_name}, size: {file_size} bytes")

    try:
        return send_file(file_path, mimetype='application/zip', as_attachment=False,
                         download_name=file_name, max_age=3600)
    except Exception as e:
        print(f"Error serving file: {e}")
        return f"Error: {str(e)}", 500


@app.route('/v2/account', methods=['GET', 'PUT'])
def account():
    if request.method == 'PUT':
        response = jsonify({})
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate'
        response.headers['Content-Type'] = 'application/json'
        response.headers['Grpc-Metadata-Content-Type'] = 'application/grpc'
        return response

    try:
        ip = get_client_ip()
        user, banned = get_or_create_user(ip)

        if banned or user is None:
            print(f"[ERROR] User banned or None - IP: {ip}, banned: {banned}, user: {user}")
            raise Exception('User is banned or DB failed')

        username = 'XERA COMPANY'
        if is_trusted_ip(ip):
            username = 'ALEX [HELPER]'

        return jsonify({
            'user': {
                'id': '2e8aace0-282d-4c3d-b9d4-6a3b3ba2c2a6',
                'username': username,
                'lang_tag': 'en',
                'metadata': json.dumps({'isDeveloper': str(is_trusted_ip(ip))}),
                'edge_count': 4,
                'create_time': '2024-08-24T07:30:12Z',
                'update_time': '2025-04-05T21:00:27Z'
            },
            'wallet': '{"stashCols": 16, "stashRows": 8, "hardCurrency": 0, "softCurrency": 20000000, "researchPoints": 69420}',
            'custom_id': user['custom_id']
        })

    except Exception as e:
        print(f"[FALLBACK] DB failed or user banned: {e}")
        import traceback
        traceback.print_exc()
        return jsonify(STATIC_ACCOUNT_RESPONSE)


@app.route('/v2/account/alt2', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
def account_alt2():
    return jsonify(STATIC_STORAGE_OBJECTS)


@app.route('/v2/account/link/device', methods=['POST'])
def link_device():
    return jsonify({
        'id': secrets.token_hex(16),
        'user_id': '13b8dce4-2c8e-4945-90b6-19af0c2b0ad7',
        'linked': True,
        'create_time': '2025-01-15T18:08:45Z'
    })


@app.route('/v2/account/session/refresh', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
def session_refresh():
    return jsonify(generate_token_pair() if GENERATE_FRESH_TOKENS else STATIC_TOKEN_PAIR)


@app.route('/v2/rpc/attest.start', methods=['POST'])
def attest_start():
    return jsonify({'payload': json.dumps({
        'status': 'success',
        'attestResult': 'Valid',
        'message': 'Attestation validated'
    })})


@app.route('/v2/storage', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
def storage():
    if request.method == 'POST':
        try:
            data = request.get_json(force=True)
            if data and 'object_ids' in data:
                user_id = data['object_ids'][0].get('user_id') if data['object_ids'] else None
                if user_id:
                    response_objects = []
                    for obj in STATIC_STORAGE_OBJECTS['objects']:
                        new_obj = obj.copy()
                        new_obj['user_id'] = user_id
                        if obj.get('key') == 'gameplay_loadout':
                            payload = generate_gameplay_loadout()
                            new_obj['value'] = payload['objects'][0]['value']
                        response_objects.append(new_obj)
                    return jsonify({'objects': response_objects})
                else:
                    return jsonify({'objects': []})
            else:
                return jsonify({'objects': []})
        except Exception as e:
            print(f"Storage error: {e}")
            return jsonify({'objects': []})

    return jsonify(STATIC_STORAGE_OBJECTS)


@app.route('/v2/storage/econ_gameplay_items', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
def econ_gameplay_items():
    return jsonify(ECON_ITEMS_RESPONSE)


@app.route('/v2/rpc/mining.balance', methods=['GET'])
def mining_balance():
    return jsonify({'payload': json.dumps({'hardCurrency': 20000000, 'researchPoints': 999999})}), 200


@app.route('/v2/rpc/purchase.list', methods=['GET'])
def purchase_list():
    return jsonify({'payload': json.dumps({
        'purchases': [
            {
                'user_id': '13b8dce4-2c8e-4945-90b6-19af0c2b0ad7',
                'product_id': 'RESEARCH_PACK',
                'transaction_id': '540282689176766',
                'store': 3,
                'purchase_time': {'seconds': 1741450711},
                'create_time': {'seconds': 1741450837, 'nanos': 694669000},
                'update_time': {'seconds': 1741450837, 'nanos': 694669000},
                'refund_time': {},
                'provider_response': json.dumps({'success': True}),
                'environment': 2
            },
            {
                'user_id': '13b8dce4-2c8e-4945-90b6-19af0c2b0ad7',
                'product_id': 'G.O.A.T_BUNDLE',
                'transaction_id': '540281232510245',
                'store': 3,
                'purchase_time': {'seconds': 1741450591},
                'create_time': {'seconds': 1741450722, 'nanos': 851245000},
                'update_time': {'seconds': 1741450722, 'nanos': 851245000},
                'refund_time': {},
                'provider_response': json.dumps({'success': True}),
                'environment': 2
            }
        ]
    })}), 200


@app.route('/v2/rpc/clientBootstrap', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
def client_bootstrap():
    return jsonify(CLIENT_BOOTSTRAP_RESPONSE)


@app.route('/auth', methods=['GET', 'POST'])
def photon_auth():
    auth_token = request.args.get('auth_token')
    print('🔐 Photon Auth Request Received')

    if auth_token:
        print(f"auth_token: {auth_token}")
        message = 'Authentication successful'
    else:
        print('⚠️ No auth_token provided')
        message = 'Authenticated without token'

    return jsonify({
        'ResultCode': 1,
        'Message': message,
        'UserId': secrets.token_hex(16),
        'SessionID': secrets.token_hex(12),
        'Authenticated': True
    }), 200


@app.route('/debug', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
def debug():
    method = request.method
    url = request.url
    headers = dict(request.headers)
    body = request.get_data(as_text=True)

    message = {
        'content': '📡 **/debug request received**',
        'embeds': [{
            'title': 'Request Info',
            'fields': [
                {'name': 'Method', 'value': method, 'inline': True},
                {'name': 'URL', 'value': url, 'inline': False},
                {'name': 'Headers', 'value': f"```json\n{json.dumps(headers, indent=2)}```", 'inline': False},
                {'name': 'Body', 'value': f"```json\n{body}```" if body else '*(empty)*', 'inline': False}
            ],
            'color': 65484
        }]
    }

    try:
        requests.post(DISCORD_WEBHOOK_URL, json=message)
    except Exception as e:
        return f"Failed to send to Discord: {e}", 500

    return 'Sent debug to discord', 200


if __name__ == '__main__':
    app.run(debug=False)
