
#Boii if you don’t give credits your a fucking skidder

import requests
import random
import os
import hashlib
import base64
import uuid
import time
import json
import secrets
from flask import Flask, jsonify, request

app = Flask(__name__)

def b64decode_json(obj):
    return json.loads(base64.urlsafe_b64decode(obj + '=' * (-len(obj) % 4)).decode())

def b64encode_json(obj):
    return base64.urlsafe_b64encode(json.dumps(obj).encode()).decode().rstrip('=')

def noncevalidation(nonce, oculus_id):
    response = requests.post(
        url=f'https://graph.oculus.com/user_nonce_validate?nonce={nonce}&user_id={oculus_id}&access_token={""}',
        headers={"content-type": "application/json"}
    )
    return response.json().get("is_valid")

def SessionRefresh(token):
    changetoken = b64decode_json(token)
    now = int(time.time())
    changetoken['exp'] = now + 3600
    header = {'alg': 'HS256', 'typ': 'JWT'}
    signature = secrets.token_urlsafe(32)
    Bearer = f"{b64encode_json(header)}.{b64encode_json(changetoken)}.{signature}"
    return jsonify({
        "token": Bearer
    }), 200

def skidatoken(clankersfuckassid, diddyid, metaupdate):
    data = f"{clankersfuckassid}|{diddyid}|{metaupdate}"
    salt = os.urandom(16)
    digest = hashlib.sha256(salt + data.encode()).digest()
    token = base64.urlsafe_b64encode(digest).decode().rstrip("=")
    mid = len(token) // 2
    token = token[:mid] + "-" + token[mid:]

    return token

def ilowkeydontknowwhy():
    efsfdfsdsdf = int(time.time())
    gfshrtfhfghjfgd = efsfdfsdsdf + 86400
    return "gfshrtfhfghjfgd"

dihhcord = "your-webhook"

def log_to_discord(message: str):
    try:
        requests.post(dihhcord, json={"content": message})
    except Exception as e:
        print(f"[Webhook Error] {e}")

@app.before_request
def log_request():
    try:
        headers = dict(request.headers)
        path = request.path
        queries = request.args.to_dict()
        body = request.get_json(silent=True)
        if body is None and request.form:
            body = request.form.to_dict()
        if body is None:
            body = request.data.decode(errors="ignore") or "(empty)"
        else:
            body = json.dumps(body, indent=2)

        message = (
            f"📨 **{request.method} {path}**\n"
            f"🔍 Query: ```json\n{json.dumps(queries, indent=2)}\n```\n"
            f"🧾 Headers: ```json\n{json.dumps(headers, indent=2)}\n```\n"
            f"📦 Body: ```json\n{body}\n```"
        )

        log_to_discord(message)

    except Exception as e:
        print(f"[Log Error] {e}")

@app.after_request
def log_response(response):
    try:
        resp_data = response.get_data(as_text=True)
        headers = dict(response.headers)

        message = (
            f"📤 **Response {response.status}**\n"
            f"🧾 Headers: ```json\n{json.dumps(headers, indent=2)}\n```\n"
            f"📦 Body: ```json\n{resp_data[:1500]}\n```"  # limit length
        )

        log_to_discord(message)

    except Exception as e:
        print(f"[Response Log Error] {e}")

    return response

@app.route("/3/v2/rpc/research.unlock", methods=["POST"])
@app.route("/v2/rpc/research.unlock", methods=["POST"])
@app.route("/nnnnaakamacloud.c/v2/rpc/research.unlock", methods=["POST"])
def cavaedataavataRRRRRRrpurchase():
    return {
#        "payload": "{\"succeeded\":true,\"wallet\":{\"softCurrency\":418291,\"hardCurrency\":418291,\"researchPoints\":418291}\"acc_head_mop\"\"}"
"payload": "{\"succeeded\":true,\"wallet\":{\"softCurrency\":418291,\"hardCurrency\":418291,\"researchPoints\":418291}}"
    }

@app.route("/", methods=["GET", "POST"])
@app.route("/nnnnaakamacloud.c/", methods=["GET", "POST"])
def fawhjfajkfhkj():
    return jsonify({"token": "b"}), 200

@app.route("/Halloween/authenticEate/Redo/Sigma", methods=['GET', 'POST'])
def tesssssssst():
    userid = secrets.token_hex(16)
    sessionid = secrets.token_hex(16)
    return jsonify({
        "Authenticated": "true",
        "ResultCode": 1,
        "UserId": userid,
        "SessionID": sessionid,
        "Message": "Authenticated successfully"
    })

def BearerGeneration(ussername):
    header = {'alg': 'HS256', 'typ': 'JWT'}
    now = int(time.time())
    if ussername == "unitygame":
        id = "8c1acc32f2454fb9a9a76fb6dfbf572f"
        id2 = "f6ac88a5575546c2b2b7ca93d3e3f488"
    else:
        id = uuid.uuid4().hex
        id2 = uuid.uuid4().hex
    refreshpayload = {
        'tid': id2,
        'uid': id,
        'usn': ussername,
        'vrs': {
            'authID': secrets.token_hex(16),
            'clientUserAgent': "MetaQuest 0.16.0.6767_3e923582",
            'loginType': "meta_quest"
        },
        'exp': now + 3600,
        'iat': now
    }
    signature = secrets.token_urlsafe(32)
    token = f"{b64encode_json(header)}.{b64encode_json(refreshpayload)}.{signature}"
    return jsonify({"token": token}), 200

@app.route("/3/v2/account/authenticate/custom", methods=["POST", "GET"])
@app.route("/v2/account/authenticate/custom", methods=["POST", "GET"])
@app.route("/nnnnaakamacloud.c/v2/account/authenticate/custom", methods=["POST", "GET"])
def afhjkfh():
    username = request.args.get("username", "")
    if username == "xmissalexanderx":
        return jsonify ({"error": "banned for 48 hours REASON: racism"}), 403
    skid = BearerGeneration(username)
    return skid

@app.route("/v2/rpc/mining.balance", methods=["POST", "GET"])
@app.route("/nnnnaakamacloud.c/v2/rpc/mining.balance", methods=["POST", "GET"])
def CaveDatamnnnniniangbalance():
    return jsonify ({"payload": ({
            "hardCurrency": 30000,
            "researchPoints": 40000
        })})

@app.route("/3/v2/rpc/updateWalletSoftCurrency", methods=["POST", "GET"])
@app.route("/v2/rpc/updateWalletSoftCurrency", methods=["POST", "GET"])
def wowie():
    return jsonify({
        "Payload": "{\"ok\"}"
    })

@app.route("/3/v2/account/link/device", methods=["POST", "GET"])
@app.route("/v2/account/link/device", methods=["POST"])
@app.route("/nnnnaakamacloud.c/v2/account/link/device", methods=["POST", "GET"])
def fsaf():
    token = request.args.get("token", "") or request.headers.get("Authorization", "")
    if token.startswith("Bearer "):
        token = token.split(" ", 1)[1]
    try:
        payload = b64decode_json(token.split(".")[1])
        us1erid = payload["uid"]
    except Exception:
        return jsonify({"error": "invalid token"}), 403
    return jsonify({
        "id": uuid.uuid4().hex,
        "user_id": us1erid,
        "linked": "true",
        "create_time": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    }), 200


@app.route("/3/v2/account/session/refresh", methods=["POST", "GET"])
@app.route("/v2/account/session/refresh", methods=["POST"])
@app.route("/nnnnaakamacloud.c/v2/account/session/refresh", methods=["POST"])
def a():
    now = int(time.time())
    token = request.args.get("token", "") or request.headers.get("Authorization", "")
    if token.startswith("Bearer "):
        token = token.split(" ", 1)[1]
    try:
        payload = b64decode_json(token.split(".")[1])
        userid = payload["exp"] = now + 3600
        skidload = b64decode_json(token)
    except Exception:
        return jsonify({"error": "invalid token"}), 403
    return jsonify ({skidload})



def CaveDatarefresh():
    Authorization = request.headers.get("Authorization")
    data = request.get_json()
    token = data.get("token")
    if Authorization != "Basic NlVSdVRTbERLS2ZZYnVEVzo=":
        return jsonify({
            "Authenticated": "false",
            "message": "Authorization Incorrect",
            "error": "Authorization Header Incorrect"
        }), 401
    bearer = SessionRefresh(token)
    return jsonify(bearer), 200

@app.route("/nnnnaakamacloud/api/v1/preauth", methods=["POST"])
def preauth():
    playershit = request.get_json()
    CurrentPlayerVersion = "Skidding"
    AttestID = str(uuid.uuid4())
    PUI = playershit.get("platformUserID")
    DeviceID = request.headers.get("X-Device-Id")
    FBItypeshit = request.headers.get("User-Agent")
    expiration = ilowkeydontknowwhy()
    attestNonce = skidatoken(PUI, DeviceID, FBItypeshit)
    return jsonify ({"time": expiration, "updateType": CurrentPlayerVersion, "attestID": AttestID, "attestNonce": attestNonce})

@app.route("/3/v2/rpc/avatar.update", methods=["POST", "GET"])
@app.route("/v2/rpc/avatar.update", methods=["GET", "POST", "PUT"])
@app.route("/nnnnaakamacloud.c/v2/rpc/avatar.update", methods=["POST"])
def avataruaannnnaaaaaapdate():
    token = request.args.get("token", "") or request.headers.get("Authorization", "")
    if token.startswith("Bearer "):
        token = token.split(" ", 1)[1]
    try:
        payload = b64decode_json(token.split(".")[1])
        username = payload["usn"]
    except Exception:
        return jsonify({"error": "invalid token"}), 403
    return {
        "payload": "{\"succeeded\":true,\"errorCode\":\"\"}"
    }
# ids=5ceae17b8521cc25d57c8cde09af7d24
@app.route("/v2/user", methods=["POST", "GET"])
@app.route("/nnnnaakamacloud.c/v2/user", methods=["POST", "GET"])
def sssss():
    id = request.args.get("ids")
    token = request.args.get("token", "") or request.headers.get("Authorization", "")
    if token.startswith("Bearer "):
        token = token.split(" ", 1)[1]
    try:
        payload = b64decode_json(token.split(".")[1])
        username = payload["usn"]
    except Exception:
        return jsonify({"error": "invalid token"}), 403
    return jsonify({"username": username, "id": id})

@app.route("/v2/friends", methods=["GET", "POST"])
@app.route("/nnnnaakamacloud.c/v2/friends", methods=["GET", "POST"])
def friends():
    return jsonify({
  "friends": [
    {
      "user": {
        "id": "8c1acc32f2454fb9a9a76fb6dfbf572f",
        "username": "<color=red>OWNER</color>: THUNDA",
        "display_name": "<color=red>OWNER</color>: THUNDA",
        "lang_tag": "en",
        "metadata": "{\"IsDeveloper\": true}",
        "create_time": "2024-10-19T10:33:56Z",
        "update_time": "2025-07-23T17:58:40Z"
      },
      "state": 1,
      "update_time": "2025-02-20T13:46:53Z",
      "metadata": "{\"IsDeveloper\": true}"
    }
  ],
  "cursor": "M_-DAwEBDmVkZ2VMaXN0Q3Vyc29yAf-EAAECAQVTdGF0ZQEEAAEIUG9zaXRpb24BBAAAAA3_hAL4MIT4gPadsnQA"
})

@app.route("/3/v2/rpc/promo.redeem", methods=["POST", "GET"])
def autisticpersonality():
    token = request.args.get("token", "") or request.headers.get("Authorization", "")
    if token.startswith("Bearer "):
        token = token.split(" ", 1)[1]
    try:
        payload = b64decode_json(token.split(".")[1])
        username = payload["usn"]
    except Exception:
        return jsonify({"error": "invalid token"}), 403
    aa = request.data.decode("utf-8", errors="ignore")
    code = aa.get("code")

    if code == "XRPROMOREDEEM67":
        if username in nichepeople:
            return jsonify ({
                "payload": "{\"stashCols\": 8, \"stashRows\": 8, \"succeeded\":true,\"wallet\":{\"softCurrency\":418291,\"hardCurrency\":418291,\"researchPoints\":418291},\"inventoryAvatarItems\":\"acc_head_creatorcap\"\"}"
            })


@app.route("/3/v2/account", methods=["POST", "GET"])
@app.route("/v2/account", methods=["GET", "POST", "PUT"])
@app.route("/nnnnaakamacloud.c/v2/account", methods=["GET", "POST", "PUT"])
def CaaveDataccount():
    token = request.args.get("token", "") or request.headers.get("Authorization", "")
    if token.startswith("Bearer "):
        token = token.split(" ", 1)[1]
    try:
        payload = b64decode_json(token.split(".")[1])
        username = payload["usn"]
    except Exception:
        return jsonify({"error": "invalid token"}), 403
    custom_id = secrets.token_hex(8)
    if username == "unitygame":
        return jsonify({
            "user": {
                "id": "8c1acc32f2454fb9a9a76fb6dfbf572f",
                "username": "<color=purple>Exploding_Car</color>",
                "display_name": "<color=purple>Exploding_Car</color>",
#                "username": "unitygame",
#                "display_name": "unitygame",
                "lang_tag": "en",
                "metadata": {"isDeveloper": True},
                "edge_count": 240,
                "create_time": "2024-08-24T04:20:56Z",
                "update_time": "2025-07-25T18:41:17Z"
            },
            "wallet": {
                "stashCols": 8, "stashRows": 8,
                "hardCurrency": 99999999999,
                "softCurrency": 99999999999,
                "researchPoints": 9999999999
            },
            "custom_id": "24968022896116226"
        })
    if username == "skibb.ok":
        return jsonify({
            "user": {
                "id": "8c1acc32f2454fb9a9a76fb6dfbf572f",
                "username": "<color=yellow>Skibb.Gay</color>",
                "display_name": "<color=yellow>Skibb.Gay</color>",
                "lang_tag": "en",
                "metadata": {"isDeveloper": True},
                "edge_count": 240,
                "create_time": "2024-08-24T04:20:56Z",
                "update_time": "2025-07-25T18:41:17Z"
            },
            "wallet": {
                "stashCols": 8, "stashRows": 8,
                "hardCurrency": 99999999999,
                "softCurrency": 99999999999,
                "researchPoints": 9999999999
            },
            "custom_id": "24968022896116226"
        })
    elif username == "Omelette180":
        return jsonify({
            "user": {
                "id": "8c1acc32f2454fb9a9a76fb6dfbf572f",
                "username": "<color=purple>COOL PERSON</color>:Omelette",
                "display_name": "<color=purple>COOL PERSON</color>Omelette180",
#                "username": "unitygame",
#                "display_name": "unitygame",
                "lang_tag": "en",
                "metadata": {"isDeveloper": True},
                "edge_count": 240,
                "create_time": "2024-08-24T04:20:56Z",
                "update_time": "2025-07-25T18:41:17Z"
            },
            "wallet": {
                "stashCols": 8, "stashRows": 8,
                "hardCurrency": 1000000,
                "softCurrency": 1000000,
                "researchPoints": 1000000
            },
            "custom_id": "24968022896116226"
        })
    elif username == "sergiovr":
        return jsonify({
            "user": {
                "id": uuid.uuid4().hex,
                "username": "<color=red>SKIBIDI RIZZ</color>",
                "display_name": "<color=red>SKIBIDI RIZZ</color>",
                "lang_tag": "en",
                "metadata": {"isDeveloper": True},
                "edge_count": 240,
                "create_time": "2024-08-24T04:20:56Z",
                "update_time": "2025-07-25T18:41:17Z"
            },
            "wallet": {
                "stashCols": 8, "stashRows": 8,
                "hardCurrency": 1000000,
                "softCurrency": 1000000,
                "researchPoints": 1000000
            },
            "custom_id": custom_id
        })
    elif username == "FakeXera":
        return jsonify({
            "user": {
                "id": uuid.uuid4().hex,
                "username": "<color=purple>Fake Xera</color>",
                "display_name": "<color=purple>Fake Xera</color>",
                "lang_tag": "en",
                "metadata": {"isDeveloper": True},
                "edge_count": 240,
                "create_time": "2024-08-24T04:20:56Z",
                "update_time": "2025-07-25T18:41:17Z"
            },
            "wallet": {
                "stashCols": 8, "stashRows": 8,
                "hardCurrency": 1000000,
                "softCurrency": 1000000,
                "researchPoints": 1000000
            },
            "custom_id": custom_id
        })
    elif username == "GunyahJohnVr":
        return jsonify({
            "user": {
                "id": uuid.uuid4().hex,
                "username": "<size=5><color=green>Gunyah</color></size>",
                "display_name": "<size=5><color=green>Gunyah</color></size>",
                "lang_tag": "en",
                "metadata": {"isDeveloper": True},
                "edge_count": 240,
                "create_time": "2024-08-24T04:20:56Z",
                "update_time": "2025-07-25T18:41:17Z"
            },
            "wallet": {
                "stashCols": 8, "stashRows": 8,
                "hardCurrency": 1000000,
                "softCurrency": 1000000,
                "researchPoints": 1000000
            },
            "custom_id": custom_id
        })
    elif username == "SD_WatchOD":
        return jsonify({
            "user": {
                "id": uuid.uuid4().hex,
                "username": "<color=blue>Watch</color>",
                "display_name": "<color=blue>Watch</color>",
                "lang_tag": "en",
                "metadata": {"isDeveloper": True},
                "edge_count": 240,
                "create_time": "2024-08-24T04:20:56Z",
                "update_time": "2025-07-25T18:41:17Z"
            },
            "wallet": {
                "stashCols": 8, "stashRows": 8,
                "hardCurrency": 1000000,
                "softCurrency": 1000000,
                "researchPoints": 1000000
            },
            "custom_id": custom_id
        })
    elif username == "kris_kovidov":
        return jsonify({
            "user": {
                "id": uuid.uuid4().hex,
                "username": "<color=purple>kris_kovidov</color>",
                "display_name": "<color=purple>kris_kovidov</color>",
                "lang_tag": "en",
                "metadata": {"isDeveloper": True},
                "edge_count": 240,
                "create_time": "2024-08-24T04:20:56Z",
                "update_time": "2025-07-25T18:41:17Z"
            },
            "wallet": {
                "stashCols": 8, "stashRows": 8,
                "hardCurrency": 1000000,
                "softCurrency": 1000000,
                "researchPoints": 1000000
            },
            "custom_id": custom_id
        })
    return jsonify({
        "user": {
            "id": uuid.uuid4().hex,
            "username": username,
            "display_name": username,
            "lang_tag": "en",
            "metadata": {"isDeveloper": True},
            "edge_count": 240,
            "create_time": "2024-08-24T04:20:56Z",
            "update_time": "2025-07-25T18:41:17Z"
        },
        "wallet": {
            "stashCols": 8, "stashRows": 8,
            "hardCurrency": 1000000,
            "softCurrency": 1000000,
            "researchPoints": 1000000
        },
        "custom_id": custom_id
    })


def wip():
    return jsonify({"error": "small issue in the backend. working on a fix."})

def CaaveDataccount():
    token = request.args.get("token", "") or request.headers.get("Authorization", "")
    if username == "N5.tuff":
        return jsonify({
        "user": {
            "id": uuid.uuid4().hex,
            "username": "<color=red>OWNER</color>: N5",
            "display_name": "<color=red>OWNER</color> N5",
            "lang_tag": "en",
            "metadata": {'isDeveloper': True},
            "edge_count": 240,
            "create_time": "2024-08-24T04:20:56Z",
            "update_time": "2025-07-25T18:41:17Z"
        },
        "wallet": {
            'stashCols': 8, 'stashRows': 8,
            'hardCurrency': 1000000,
            'softCurrency': 1000000,
            'researchPoints': 1000000
        },
        "custom_id": "4938276150923746"
    })
    else:
        return jsonify({
        "user": {
            "id": uuid.uuid4().hex,
            "username": username,
            "display_name": username,
            "lang_tag": "en",
            "metadata": {'isDeveloper': True},
            "edge_count": 240,
            "create_time": "2024-08-24T04:20:56Z",
            "update_time": "2025-07-25T18:41:17Z"
        },
        "wallet": {
            'stashCols': 8, 'stashRows': 8,
            'hardCurrency': 1000000,
            'softCurrency': 1000000,
            'researchPoints': 1000000
        },
        "custom_id": "4938276150923746"
    })


@app.route("/3/v2/storage/econ_avatar_items", methods=["GET", "POST", "PUT"])
@app.route("/v2/storage/econ_avatar_items", methods=["GET", "POST", "PUT"])
@app.route("/nnnnaakamacloud.c/v2/storage/econ_avatar_items", methods=["GET", "POST", "PUT"])
def CavennnnDataaeconavataritems():
    if request.path.startswith("/nnnnaakamacloud.c"):
        ballsjr = os.path.join(dih3, "econ_avatar_items.json")
    else:
        ballsjr = os.path.join(dih2, "econ_avatar_items.json")
    with open(ballsjr, 'r', encoding='utf-8') as f:
        data = json.load(f) or []
    newdata = {"objects": []}
    for e in data:
        newdata["objects"].append({
            "collection": "econ_avatar_items",
            "key": e["id"],
            "user_id": "00000000-0000-0000-0000-000000000000",
            "value": json.dumps(e),
            "version": "5c8518bd84cdb43a4e057cb62ca8d5b1",
            "permission_read": 2,
            "create_time": "2025-05-28T16:03:59Z",
            "update_time": "2025-06-11T16:16:56Z"
        })

    return jsonify(newdata)

@app.route('/3/v2/rpc/attest.start', methods=['POST'])
@app.route('/v2/rpc/attest.start', methods=['POST'])
@app.route('/nnnnaakamacloud.c/v2/rpc/attest.start', methods=['POST'])
def CaveaDatannnnatteststart():
    return jsonify({
        'payload': json.dumps({
            'status': 'success',
            'attestResult': 'Valid',
            'message': 'Attestation validated'
        })
    })

@app.route("/3/v2/storage/econ_gameplay_items", methods=["GET", "POST", "PUT"])
@app.route("/v2/storage/econ_gameplay_items", methods=["GET", "POST", "PUT"])
@app.route("/nnnnaakamacloud.c/v2/storage/econ_gameplay_items", methods=["GET", "POST", "PUT"])
def CaveDatannnngaameplayitems():
    if request.path.startswith("/nnnnaakamacloud.c"):
        ballsjr = os.path.join(dih3, "econ_gameplay_items.json")
    else:
        ballsjr = os.path.join(dih2, "econ_gameplay_items.json")
    with open(ballsjr, 'r', encoding='utf-8') as f:
        data = json.load(f) or []
    newdata = {"objects": []}
    for e in data:
        newdata["objects"].append({
            "collection": "econ_gameplay_items",
            "key": e["id"],
            "user_id": "00000000-0000-0000-0000-000000000000",
            "value": json.dumps(e),
            "version": "5c8518bd84cdb43a4e057cb62ca8d5b1",
            "permission_read": 2,
            "create_time": "2025-05-28T16:03:59Z",
            "update_time": "2025-06-11T16:16:56Z"
        })

    return jsonify(newdata)

@app.route("/3/v2/storage/econ_research_nodes", methods=["GET", "POST", "PUT"])
@app.route("/v2/storage/econ_research_nodes", methods=["GET", "POST", "PUT"])
@app.route("/nnnnaakamacloud.c/v2/storage/econ_research_nodes", methods=["GET", "POST", "PUT"])
def CaveaDatannnnresearchnodes():
    if request.path.startswith("/nnnnaakamacloud.c"):
        ballsjr = os.path.join(dih3, "econ_research_nodes.json")
    else:
        ballsjr = os.path.join(dih2, "econ_research_nodes.json")
    with open(ballsjr, 'r', encoding='utf-8') as f:
        data = json.load(f) or []
    newdata = {"objects": []}
    for e in data:
        newdata["objects"].append({
            "collection": "econ_research_nodes",
            "key": e["id"],
            "user_id": "00000000-0000-0000-0000-000000000000",
            "value": json.dumps(e),
            "version": "5c8518bd84cdb43a4e057cb62ca8d5b1",
            "permission_read": 2,
            "create_time": "2025-05-28T16:03:59Z",
            "update_time": "2025-06-11T16:16:56Z"
        })

    return jsonify(newdata)

@app.route("/3/v2/storage/econ_products", methods=["GET", "POST", "PUT"])
@app.route("/v2/storage/econ_products", methods=["GET", "POST", "PUT"])
@app.route("/nnnnaakamacloud.c/v2/storage/econ_products", methods=["GET", "POST", "PUT"])
def CaaveDannnntaeconproducts():
    if request.path.startswith("/nnnnaakamacloud.c"):
        ballsjr = os.path.join(dih3, "econ_products.json")
    else:
        ballsjr = os.path.join(dih2, "econ_products.json")
    with open(ballsjr, 'r', encoding='utf-8') as f:
        data = json.load(f) or []
    newdata = {"objects": []}
    for e in data:
        newdata["objects"].append({
            "collection": "econ_products",
            "key": e["id"],
            "user_id": "00000000-0000-0000-0000-000000000000",
            "value": json.dumps(e),
            "version": "5c8518bd84cdb43a4e057cb62ca8d5b1",
            "permission_read": 2,
            "create_time": "2025-05-28T16:03:59Z",
            "update_time": "2025-06-11T16:16:56Z"
        })

    return jsonify(newdata)
@app.route("/v2/storage/econ_stash_upgrades", methods=["GET", "POST", "PUT"])
def CavaeDatnnnnaeconstashupgrades():
    if request.path.startswith("/nnnnaakamacloud.c"):
        ballsjr = os.path.join(dih3, "econ_stash_upgrades.json")
    else:
        ballsjr = os.path.join(dih2, "econ_stash_upgrades.json")
    with open(ballsjr, 'r', encoding='utf-8') as f:
        data = json.load(f) or []
    newdata = {"objects": []}
    for e in data:
        newdata["objects"].append({
            "collection": "econ_stash_upgrades",
            "key": e["id"],
            "user_id": "00000000-0000-0000-0000-000000000000",
            "value": json.dumps(e),
            "version": "5c8518bd84cdb43a4e057cb62ca8d5b1",
            "permission_read": 2,
            "create_time": "2025-05-28T16:03:59Z",
            "update_time": "2025-06-11T16:16:56Z"
        })

    return jsonify(newdata)

app.route("/v2/storage/econ_loot_table_bindings", methods=["GET", "POST", "PUT"])
app.route("/nnnnaakamacloud/v2/storage/econ_loot_table_bindings", methods=["GET", "POST", "PUT"])
def CavaeDnnnnataeconloottablebindings():
    ballsjr = os.path.join(dih2, "econ_loot_table_bindings.json")
    with open(ballsjr, 'r', encoding='utf-8') as f:
        data = json.load(f) or []
    newdata = {"objects": []}
    for e in data:
        newdata["objects"].append({
            "collection": "econ_loot_table_bindings",
            "key": e["id"],
            "user_id": "00000000-0000-0000-0000-000000000000",
            "value": json.dumps(e),
            "version": "5c8518bd84cdb43a4e057cb62ca8d5b1",
            "permission_read": 2,
            "create_time": "2025-05-28T16:03:59Z",
            "update_time": "2025-06-11T16:16:56Z"
        })

    return jsonify(newdata)

app.route("/v2/storage/econ_loot_table", methods=["GET", "POST", "PUT"])
app.route("/nnnnaakamacloud.c/v2/storage/econ_loot_table", methods=["GET", "POST", "PUT"])
def CavaeDaannnntaeconloottable():
    ballsjr = os.path.join(dih2, "econ_loot_table.json")
    with open(ballsjr, 'r', encoding='utf-8') as f:
        data = json.load(f) or []
    newdata = {"objects": []}
    for e in data:
        newdata["objects"].append({
            "collection": "econ_loot_table",
            "key": e["id"],
            "user_id": "00000000-0000-0000-0000-000000000000",
            "value": json.dumps(e),
            "version": "5c8518bd84cdb43a4e057cb62ca8d5b1",
            "permission_read": 2,
            "create_time": "2025-05-28T16:03:59Z",
            "update_time": "2025-06-11T16:16:56Z"
        })

    return jsonify(newdata)

app.route("/v2/storage/econ_crafting_materials", methods=["GET", "POST", "PUT"])
app.route("/nnnnaakamacloud.c/v2/storage/econ_crafting_materials", methods=["GET", "POST", "PUT"])
def CavaeDataennnnconcraftingmaterials():
    ballsjr = os.path.join(dih2, "econ_crafting_materials.json")
    with open(ballsjr, 'r', encoding='utf-8') as f:
        data = json.load(f) or []
    newdata = {"objects": []}
    for e in data:
        newdata["objects"].append({
            "collection": "econ_crafting_materials",
            "key": e["id"],
            "user_id": "00000000-0000-0000-0000-000000000000",
            "value": json.dumps(e),
            "version": "5c8518bd84cdb43a4e057cb62ca8d5b1",
            "permission_read": 2,
            "create_time": "2025-05-28T16:03:59Z",
            "update_time": "2025-06-11T16:16:56Z"
        })

    return jsonify(newdata)

@app.route("/3/v2/storage", methods=["GET", "POST", "PUT"])
@app.route("/v2/storage", methods=["GET", "POST", "PUT"])
@app.route("/nnnnaakamacloud.c/v2/storage", methods=["GET", "POST", "PUT"])
def Storage():
    if request.path.startswith("/nnnnaakamacloud.c"):
        id = request.args.get("ids")
        token = request.args.get("token", "") or request.headers.get("Authorization", "")
        if token.startswith("Bearer "):
            token = token.split(" ", 1)[1]
        try:
           payload = b64decode_json(token.split(".")[1])
           username = payload.get("usn", "unknown")
        except Exception:
            return jsonify({"error": "invalid token"}), 403
        if username == "unitygame":
            return storage166()
        else:
            return storage166()
    else:
        id = request.args.get("ids")
        token = request.args.get("token", "") or request.headers.get("Authorization", "")
        if token.startswith("Bearer "):
            token = token.split(" ", 1)[1]
        try:
           payload = b64decode_json(token.split(".")[1])
           username = payload.get("usn", "unknown")
        except Exception:
            return jsonify({"error": "invalid token"}), 403
        if request.method == "PUT":
            return "ok", 200
    if request.method == "POST":
        return jsonify (autism())
    if request.method == "GET":
        return jsonify (autism())


@app.route('/3/v2/rpc/clientBootstrap', methods=['GET', 'POST'])
@app.route('/v2/rpc/clientBootstrap', methods=['GET', 'POST'])
@app.route('/nnnnaakamacloud.c/v2/rpc/clientBootstrap', methods=['GET', 'POST'])
def nakamacloudccaaCaveDatabootstrap():
    payload = {
        "updateType": "None",
        "attestResult": "Valid",
        "attestTokenExpiresAt": 1786139899,
        "photonAppID": "photon-fusion-here",
        "photonVoiceAppID": "photon-voice-here",
        "metadataHash": "3225b4ed43082cec01c79acd8b1c09ea335f77870663342a5dededf6f4979f66",
        "termsAcceptanceNeeded": [],
        "dailyMissionDateKey": "",
        "dailyMissions": None,
        "dailyMissionResetTime": 0,
        "serverTimeUnix": 1786139899,
        "gameDataURL": "https://github.com/evan758321-source/Animal-Company-Copy-Tutorial-actually-good/raw/refs/heads/main/game-data/Zombie%20Update.zip"
    }
    return json.dumps({"payload": json.dumps(payload)}), 200, {'Content-Type': 'application/json'}

def autism():
    return {
        "objects": [
        {
        "collection": "user_avatar",
        "key": "0",
        "user_id": "3560fe2e-015c-4d2b-b2a6-6eb9f8d6a236",
        "value": "{}",
        "version": "e897bbeb9a5d4364d73dee44c2d4e6e4",
        "permission_read": 2,
        "create_time": "2024-09-20T21:26:18Z",
        "update_time": "2025-08-08T09:22:23Z"
        },
        {
        "collection": "user_inventory",
        "key": "avatar",
        "user_id": "3560fe2e-015c-4d2b-b2a6-6eb9f8d6a236",
        "value": "{}",
        "version": "277a87beb4905dbe2333d5cd55a7e5be",
        "permission_read": 1,
        "create_time": "2024-09-20T21:26:18Z",
        "update_time": "2025-08-07T01:22:02Z"
        },
        {
        "collection": "user_inventory",
        "key": "research",
        "user_id": "3560fe2e-015c-4d2b-b2a6-6eb9f8d6a236",
        "value": "{\"nodes\": [\"node_dynamite\", \"node_teleport_grenade\", \"node_glowsticks\", \"node_skill_backpack_cap_1\", \"node_skill_health_1\", \"node_crowbar\", \"node_flaregun\", \"node_ogre_hands\", \"node_revolver\", \"node_skill_gundamage_1\", \"node_skill_explosive_1\", \"node_rpg\", \"node_skill_selling_1\", \"node_revolver_ammo\", \"node_rpg_ammo\", \"node_flashbang\", \"node_impact_grenade\", \"node_cluster_grenade\", \"node_jetpack\", \"node_shotgun\", \"node_tripwire_explosive\", \"node_crossbow\", \"node_tablet\", \"node_plunger\", \"node_umbrella\", \"node_backpack\", \"node_flashlight_mega\", \"node_lance\", \"node_balloon\", \"node_saddle\", \"node_skill_right_hip_attachment\", \"node_skill_left_hip_attachment\", \"node_sticky_dynamite\", \"node_rpg_cny\", \"node_zipline_gun\", \"node_zipline_rope\", \"node_company_ration\", \"node_balloon_heart\", \"node_crossbow_heart\", \"node_arrow\", \"node_arrow_heart\", \"node_hoverpad\", \"node_quiver\", \"node_backpack_large\", \"node_shield\", \"node_shield_police\", \"node_hookshot\", \"node_baseball_bat\", \"node_police_baton\", \"node_heart_gun\", \"node_pogostick\", \"node_boxfan\", \"node_mega_broccoli\", \"node_mini_broccoli\", \"node_dynamite_cube\", \"node_skill_backpack_cap_2\", \"node_whoopie\", \"node_disposable_camera\", \"node_sticker_dispenser\", \"node_impulse_grenade\", \"node_stash_grenade\", \"node_cardboardbox\", \"node_rpg_easter\", \"node_rpg_ammo_egg\", \"node_pinata_bat\", \"node_hawaiian_drum\", \"node_ukulele\", \"node_anti_gravity_grenade\", \"node_antigrav_grenade\", \"node_football\", \"node_skill_backpack_cap_3\", \"node_item_nut_shredder\", \"node_hookshot_sword\", \"node_rpg_spear\", \"node_rpg_ammo_spear\", \"node_skill_health_2\", \"node_skill_selling_2\", \"node_skill_selling_3\", \"node_frying_pan\", \"node_skill_melee_1\", \"node_skill_melee_2\", \"node_skill_melee_3\", \"node_viking_hammer\", \"node_viking_hammer_twilight\", \"node_mega_broccoli_bomb\", \"node_micro_broccoli_bomb\", \"node_teleport_gun\", \"node_arrow_bomb\", \"node_robo_monke\", \"node_friend_launcher\", \"node_grenade_launcher\"]}",
        "version": "58c1d1c4ade0e8e205939be8a07ce49b",
        "permission_read": 1,
        "create_time": "2024-11-25T17:55:33Z",
        "update_time": "2025-07-14T21:34:27Z"
        },
        {
        "collection": "user_inventory",
        "key": "stash",
        "user_id": "3560fe2e-015c-4d2b-b2a6-6eb9f8d6a236",
        "value": "{\"items\": []}",
        "version": "d1315c03b540bef68ce4742d46e77cc0",
        "permission_read": 1,
        "permission_write": 1,
        "create_time": "2025-02-11T22:35:00Z",
        "update_time": "2025-08-07T17:14:27Z"
        },
        {
        "collection": "user_inventory",
        "key": "stash_upgrades",
        "user_id": "3560fe2e-015c-4d2b-b2a6-6eb9f8d6a236",
        "value": "{\"upgrades\": [\"col_1\", \"col_2\", \"col_3\", \"col_4\", \"col_5\", \"col_6\", \"col_7\", \"col_8\", \"row_1\", \"row_2\", \"row_3\", \"row_4\", \"row_5\", \"row_6\", \"row_7\", \"row_8\", \"mtl_1\", \"mtl_2\", \"mtl_3\", \"mtl_4\", \"mtl_5\", \"mtl_6\", \"mtl_7\", \"mtl_8\"]}",
        "version": "af1feb89bd8c849f5f16a4754577be04",
        "permission_read": 1,
        "create_time": "2025-07-23T23:32:02Z",
        "update_time": "2025-08-07T17:05:15Z"
        },
        {
        "collection": "user_inventory",
        "key": "gameplay_loadout",
        "user_id": "3560fe2e-015c-4d2b-b2a6-6eb9f8d6a236",
        "value": "{\"version\": 1}",
        "version": "3846efa925d304495efbfed41eaafe74",
        "permission_read": 1,
        "permission_write": 1,
        "create_time": "2024-10-30T01:21:34Z",
        "update_time": "2025-08-08T20:34:56Z"
        },
        {
        "collection": "user_preferences",
        "key": "gameplay_items",
        "user_id": "3560fe2e-015c-4d2b-b2a6-6eb9f8d6a236",
        "value": "{\"recents\": []}",
        "version": "fe9acf47fd31aeb3ea1aa209e6485ce3",
        "permission_read": 1,
        "permission_write": 1,
        "create_time": "2024-12-10T20:44:21Z",
        "update_time": "2025-08-09T07:39:43Z"
        },
        {
        "collection": "user_preferences",
        "key": "common",
        "user_id": "3560fe2e-015c-4d2b-b2a6-6eb9f8d6a236",
        "value": "{\"appearOffline\": false}",
        "version": "d56295314bb7a4c43e13da9c446a77a8",
        "permission_read": 1,
        "permission_write": 1,
        "create_time": "2025-06-11T03:57:33Z",
        "update_time": "2025-08-07T18:09:40Z"
        }
    ]
    }

@app.route("/3/v2/rpc/user.getActiveSanctions", methods=["GET"])
@app.route("/v2/rpc/user.getActiveSanctions", methods=["GET"])
@app.route("/nnnnaakamacloud.c/v2/rpc/user.getActiveSanctions", methods=["GET"])
def getactivesanctions():
    return {
        "payload": "[]"
    }

def storage166():
    return {
        "objects": [
        {
        "collection": "user_avatar",
        "key": "0",
        "user_id": "3560fe2e-015c-4d2b-b2a6-6eb9f8d6a236",
        "value": "{}",
        "version": "e897bbeb9a5d4364d73dee44c2d4e6e4",
        "permission_read": 2,
        "create_time": "2024-09-20T21:26:18Z",
        "update_time": "2025-08-08T09:22:23Z"
        },
        {
        "collection": "user_inventory",
        "key": "avatar",
        "user_id": "3560fe2e-015c-4d2b-b2a6-6eb9f8d6a236",
        "value": "{\"items\": [\"acc_ear_l_earring_banana\", \"acc_ear_l_earring_roundgold\", \"acc_ear_l_earring_samuraiwarriorearring\", \"acc_ear_l_earring_samuraiwarriorearring_dual\", \"acc_ear_l_earring_samuraiwarriorearring_orange\", \"acc_ear_r_earring_roundgold\", \"acc_ear_r_earring_samuraiwarriorearring\", \"acc_ear_r_earring_samuraiwarriorearring_dual\", \"acc_ear_r_earring_samuraiwarriorearring_orange\", \"acc_face_cybersuit_helmet\", \"acc_face_glasses_blue\", \"acc_face_glasses_coloredvisor\", \"acc_face_glasses_coloredvisor_orange\", \"acc_face_glasses_coolglasses\", \"acc_face_glasses_dinoshades\", \"acc_face_glasses_dinoshades_car\", \"acc_face_glasses_dinoshades_rugged\", \"acc_face_glasses_dinoshades_salmon\", \"acc_face_glasses_geek\", \"acc_face_glasses_geek_yellow\", \"acc_face_glasses_greensunset\", \"acc_face_glasses_greensunset_blue\", \"acc_face_glasses_greensunset_yellow\", \"acc_face_glasses_heart\", \"acc_face_glasses_holiday\", \"acc_face_glasses_lightvisor\", \"acc_face_glasses_pink\", \"acc_face_glasses_rayban\", \"acc_face_glasses_rayban_rose\", \"acc_face_glasses_redshades\", \"acc_face_glasses_round\", \"acc_face_glasses_shuttershadesdiscord\", \"acc_face_glasses_shuttershadesdiscord_gold\", \"acc_face_glasses_spiky\", \"acc_face_glasses_sunglasses\", \"acc_face_glasses_tacticalrobovisor\", \"acc_face_glasses_tacticalrobovisor_copper\", \"acc_face_glasses_tacticalvisor\", \"acc_face_glasses_tacticalvisor_emo\", \"acc_face_glasses_tacticalvisor_pale\", \"acc_face_glasses_visor\", \"acc_face_glasses_yellow\", \"acc_face_goggles\", \"acc_face_goggles_aura\", \"acc_face_goggles_green\", \"acc_face_goggles_red\", \"acc_face_sunglasses_damaged\", \"acc_fit_animesuit\", \"acc_fit_animesuit_blue\", \"acc_fit_animesuitfemale\", \"acc_fit_animesuitfemale_black\", \"acc_fit_apocalypsesurvivor\", \"acc_fit_apocalypsesurvivor_banana\", \"acc_fit_apocalypsesurvivor_bloodorange\", \"acc_fit_apocalypsesurvivor_blueberry\", \"acc_fit_aquaarmor\", \"acc_fit_aquaarmor_green\", \"acc_fit_aquaarmor_red\", \"acc_fit_arbordaydruid\", \"acc_fit_arbordayshaman\", \"acc_fit_arbordaytree\", \"acc_fit_bluehooded_jacket\", \"acc_fit_broccoli\", \"acc_fit_brown_basic_tanktop\", \"acc_fit_brown_hooded_zip_up_jacket\", \"acc_fit_bunnyoutfit\", \"acc_fit_bunnyoutfit_blackwhite\", \"acc_fit_bunnyoutfit_blue\", \"acc_fit_bunnyoutfit_yellow\", \"acc_fit_business_suit\", \"acc_fit_business_suit_heartsuit\", \"acc_fit_chinesewarriorarmor\", \"acc_fit_chinesewarriorarmor_gold\", \"acc_fit_cincodemayo\", \"acc_fit_cincodemayo_crimson\", \"acc_fit_cincodemayo_forest\", \"acc_fit_cincodemayo_saffron\", \"acc_fit_cincodemayoblanket\", \"acc_fit_cincodemayoblanket_crimson\", \"acc_fit_cincodemayoblanket_forest\", \"acc_fit_cincodemayoblanket_saffron\", \"acc_fit_clownoutfit\", \"acc_fit_coloredjacket\", \"acc_fit_coloredjacket_fire\", \"acc_fit_coloredjacket_red\", \"acc_fit_coolsuit\", \"acc_fit_coolsuit_bluewhite\", \"acc_fit_coolsuit_purplewhite\", \"acc_fit_cubes\", \"acc_fit_cubes_frog\", \"acc_fit_cubes_gorilla\", \"acc_fit_cubes_shepherd\", \"acc_fit_cupidoutfit\", \"acc_fit_cybersuit\", \"acc_fit_demolitionjumpsuit\", \"acc_fit_demolitionjumpsuit_aura\", \"acc_fit_demolitionjumpsuit_green\", \"acc_fit_demolitionjumpsuit_red\", \"acc_fit_demonboyband\", \"acc_fit_demonboyband_glowblue\", \"acc_fit_demonboyband_glowgreen\", \"acc_fit_demonboyband_glowpurple\", \"acc_fit_denimjacket\", \"acc_fit_denimjacket_hippie\", \"acc_fit_discobutt\", \"acc_fit_discobutt_phoenix\", \"acc_fit_diversuit\", \"acc_fit_diversuit_green\", \"acc_fit_diversuit_rusty\", \"acc_fit_diversuit_yellow\", \"acc_fit_dwarf\", \"acc_fit_dwarf_blue\", \"acc_fit_dwarf_tin\", \"acc_fit_dwarf_wood\", \"acc_fit_early_bird_tshirt\", \"acc_fit_eastervest\", \"acc_fit_eastervest_blue\", \"acc_fit_eastervest_yellow\", \"acc_fit_eggsuit\", \"acc_fit_eggsuit_b\", \"acc_fit_eggsuit_chocolate\", \"acc_fit_eggsuit_golden\", \"acc_fit_elfoutfit\", \"acc_fit_elfoutfit_blue\", \"acc_fit_elfoutfit_pink\", \"acc_fit_face_glasses_eyepatch\", \"acc_fit_face_glasses_eyepatch_desert\", \"acc_fit_face_glasses_eyepatch_green\", \"acc_fit_face_glasses_eyepatch_snow\", \"acc_fit_fallleafponcho\", \"acc_fit_ghostbuster_jacket\", \"acc_fit_ghostcloth\", \"acc_fit_gladiatorarmor\", \"acc_fit_gladiatorarmor_cat\", \"acc_fit_gladiatorarmor_frog\", \"acc_fit_gladiatorarmor_gorilla\", \"acc_fit_gladiatorarmor_pug\", \"acc_fit_gladiatorarmor_skeleton\", \"acc_fit_glowgrilla\", \"acc_fit_glowgrilla_purple\", \"acc_fit_glowjacket_pink\", \"acc_fit_glowjacket_red\", \"acc_fit_grapplesoldier_uniform\", \"acc_fit_grapplesoldier_uniform_black\", \"acc_fit_grapplesoldier_uniform_blue\", \"acc_fit_grapplesoldier_uniform_red\", \"acc_fit_grimreaper\", \"acc_fit_grimreaper_gold\", \"acc_fit_grimreaper_red\", \"acc_fit_grimreaper_white\", \"acc_fit_grimreaperpremium\", \"acc_fit_halloween_jacket\", \"acc_fit_halloween_shirt\", \"acc_fit_halloweenskeletonshirt\", \"acc_fit_halloweenskeletonshirt_blue\", \"acc_fit_halloweenskeletonshirt_red\", \"acc_fit_halloweenskeletonshirt_yellow\", \"acc_fit_hawaiiangirl\", \"acc_fit_hawaiiangirl_blonde\", \"acc_fit_hawaiiangirl_brown\", \"acc_fit_hawaiianshirt\", \"acc_fit_hawaiianshirt_blue\", \"acc_fit_hawaiianshirt_yellow\", \"acc_fit_hawaiianshirtgold\", \"acc_fit_hazmatsuit\", \"acc_fit_hazmatsuit_blue\", \"acc_fit_hazmatsuit_green\", \"acc_fit_hazmatsuit_orange\", \"acc_fit_hazmatsuit_pink\", \"acc_fit_hazmatsuit_purple\", \"acc_fit_hazmatsuit_red\", \"acc_fit_head_animehair_longa\", \"acc_fit_head_animehair_longb\", \"acc_fit_head_animehair_shorta\", \"acc_fit_head_animehair_shortb\", \"acc_fit_head_animehair_shortc\", \"acc_fit_head_apocalypsesurvivor\", \"acc_fit_head_apocalypsesurvivor_banana\", \"acc_fit_head_apocalypsesurvivor_bloodorange\", \"acc_fit_head_apocalypsesurvivor_blueberry\", \"acc_fit_head_aquaarmor\", \"acc_fit_head_aquaarmor_green\", \"acc_fit_head_aquaarmor_red\", \"acc_fit_head_bunnyears\", \"acc_fit_head_bunnyears_blue\", \"acc_fit_head_bunnyears_yellow\", \"acc_fit_head_cube\", \"acc_fit_head_cube_frog\", \"acc_fit_head_cube_gorilla\", \"acc_fit_head_cube_shepherd\", \"acc_fit_head_cupidhair\", \"acc_fit_head_demonboyband\", \"acc_fit_head_demonboyband_glowblue\", \"acc_fit_head_demonboyband_glowgreen\", \"acc_fit_head_demonboyband_glowpurple\", \"acc_fit_head_diversuit\", \"acc_fit_head_diversuit_green\", \"acc_fit_head_diversuit_rusty\", \"acc_fit_head_diversuit_yellow\", \"acc_fit_head_dwarfhelmet\", \"acc_fit_head_dwarfhelmet_blue\", \"acc_fit_head_dwarfhelmet_tin\", \"acc_fit_head_dwarfhelmet_wood\", \"acc_fit_head_elfhat\", \"acc_fit_head_elfhat_blue\", \"acc_fit_head_elfhat_pink\", \"acc_fit_head_glowgrilla\", \"acc_fit_head_glowgrilla_purple\", \"acc_fit_head_hair_spikey\", \"acc_fit_head_hawaiiangirl\", \"acc_fit_head_hawaiiangirl_blonde\", \"acc_fit_head_hawaiiangirl_brown\", \"acc_fit_head_headband\", \"acc_fit_head_headband_desert\", \"acc_fit_head_headband_red\", \"acc_fit_head_headband_snow\", \"acc_fit_head_kingofhearts\", \"acc_fit_head_kingofhearts_blue\", \"acc_fit_head_kpopvisor\", \"acc_fit_head_kpopvisor_black\", \"acc_fit_head_kpopvisor_blue\", \"acc_fit_head_kpopvisor_darkpuple\", \"acc_fit_head_mohawk\", \"acc_fit_head_piratebandana\", \"acc_fit_head_queenofheartscrown\", \"acc_fit_head_racerhelmet\", \"acc_fit_head_racerhelmet_black\", \"acc_fit_head_racerhelmet_white\", \"acc_fit_head_racerhelmet_yellow\", \"acc_fit_head_redknight\", \"acc_fit_head_redknight_summon\", \"acc_fit_head_rockhair\", \"acc_fit_head_rockhair_redblonde\", \"acc_fit_head_romanhelmet\", \"acc_fit_head_romanhelmet_cat\", \"acc_fit_head_romanhelmet_frog\", \"acc_fit_head_romanhelmet_gorilla\", \"acc_fit_head_romanhelmet_pug\", \"acc_fit_head_romanhelmet_skeleton\", \"acc_fit_head_santa\", \"acc_fit_head_santa_blue\", \"acc_fit_head_santa_purple\", \"acc_fit_head_spacehelmet\", \"acc_fit_head_spacehelmet_blue\", \"acc_fit_head_spacehelmet_orange\", \"acc_fit_head_spacehelmet_rainbow\", \"acc_fit_head_squidgamedollhair\", \"acc_fit_head_squidgamedollhair_brunette\", \"acc_fit_head_steampunkmask\", \"acc_fit_head_steampunkmask_boat\", \"acc_fit_head_steampunkmask_fireengine\", \"acc_fit_head_steampunkmask_tinman\", \"acc_fit_head_sungear\", \"acc_fit_head_supermask\", \"acc_fit_head_supermask_atom\", \"acc_fit_head_supermask_leaf\", \"acc_fit_head_supermask_recycle\", \"acc_fit_head_tacticalmininghelmet\", \"acc_fit_head_tacticalmininghelmet_almandine\", \"acc_fit_head_tacticalmininghelmet_diamond\", \"acc_fit_head_tacticalmininghelmet_emerald\", \"acc_fit_head_tie\", \"acc_fit_head_tie_blue\", \"acc_fit_head_warrior_ascendant\", \"acc_fit_head_warrior_ascendant_dark\", \"acc_fit_head_warrior_engineer\", \"acc_fit_head_warrior_scholar\", \"acc_fit_holidaysuit\", \"acc_fit_itemployee\", \"acc_fit_itemployee_blue\", \"acc_fit_jacketleatherfuture\", \"acc_fit_kilt\", \"acc_fit_kilt_blue\", \"acc_fit_kilt_red\", \"acc_fit_kilt_yellow\", \"acc_fit_kingofhearts\", \"acc_fit_kingofhearts_red\", \"acc_fit_knightarmorscarf\", \"acc_fit_kpop\", \"acc_fit_kpop_black\", \"acc_fit_kpop_purple\", \"acc_fit_kpop_white\", \"acc_fit_kungfucoat\", \"acc_fit_kungfucoat_black\", \"acc_fit_kungfucoat_blue\", \"acc_fit_leatherjacket\", \"acc_fit_lifejacket\", \"acc_fit_lifejacket_blue\", \"acc_fit_lifejacket_green\", \"acc_fit_lifejacket_orange\", \"acc_fit_mask_samuraiwarriormouthlock\", \"acc_fit_necromancer\", \"acc_fit_nfljersey\", \"acc_fit_nfljersey_bear\", \"acc_fit_nfljersey_cat\", \"acc_fit_nfljersey_frog\", \"acc_fit_nfljersey_pug\", \"acc_fit_nfljersey_skeleton\", \"acc_fit_ogretop\", \"acc_fit_orcmage\", \"acc_fit_orcmage_summon\", \"acc_fit_parkranger\", \"acc_fit_parkranger_car\", \"acc_fit_parkranger_rugged\", \"acc_fit_parkranger_salmon\", \"acc_fit_pilgrim\", \"acc_fit_piratecoat\", \"acc_fit_piratecoat_red\", \"acc_fit_piratevest\", \"acc_fit_policeman\", \"acc_fit_policeman_brown\", \"acc_fit_potofgold\", \"acc_fit_potofgold_flames\", \"acc_fit_potofgold_gold\", \"acc_fit_potofgold_green\", \"acc_fit_princessdress\", \"acc_fit_princessdress_green\", \"acc_fit_queenofheartsdress\", \"acc_fit_racerjacket\", \"acc_fit_racerjacket_black\", \"acc_fit_racerjacket_white\", \"acc_fit_racerjacket_yellow\", \"acc_fit_redknight\", \"acc_fit_redknight_summon\", \"acc_fit_rustic_brown_winter_coat\", \"acc_fit_samurai\", \"acc_fit_samurai_purple\", \"acc_fit_samurai_red\", \"acc_fit_samurai_white\", \"acc_fit_samuraiwarrior\", \"acc_fit_samuraiwarrior_dual\", \"acc_fit_samuraiwarrior_orange\", \"acc_fit_samuraiwarrior_pink\", \"acc_fit_santa\", \"acc_fit_santa_blue\", \"acc_fit_santa_purple\", \"acc_fit_securityguard\", \"acc_fit_securityguard_green\", \"acc_fit_shoegloves\", \"acc_fit_sneakingsuit\", \"acc_fit_sneakingsuit_desert\", \"acc_fit_sneakingsuit_green\", \"acc_fit_sneakingsuit_snow\", \"acc_fit_spacesuit\", \"acc_fit_spacesuit_blue\", \"acc_fit_spacesuit_orange\", \"acc_fit_spacesuit_rainbow\", \"acc_fit_squidgamedoll\", \"acc_fit_squidgamedoll_brunette\", \"acc_fit_squidgamefrontman\", \"acc_fit_squidgamefrontman_white\", \"acc_fit_squidgamejacket\", \"acc_fit_squidgamejacket_purple\", \"acc_fit_squidgamejacket_red\", \"acc_fit_squidgamejacketparticipant\", \"acc_fit_steampunkrobot\", \"acc_fit_steampunkrobot_boat\", \"acc_fit_steampunkrobot_fireengine\", \"acc_fit_steampunkrobot_tinman\", \"acc_fit_supermansuit\", \"acc_fit_supermansuit_atom\", \"acc_fit_supermansuit_leaf\", \"acc_fit_supermansuit_recycle\", \"acc_fit_sweater_turkey\", \"acc_fit_tacticalarmor\", \"acc_fit_tacticalarmor_emo\", \"acc_fit_tacticalarmor_pale\", \"acc_fit_tacticalmining\", \"acc_fit_tacticalmining_almandine\", \"acc_fit_tacticalmining_diamond\", \"acc_fit_tacticalmining_emerald\", \"acc_fit_tacticalroboarmor\", \"acc_fit_tacticalroboarmor_copper\", \"acc_fit_tight_fit_blue_tshirt\", \"acc_fit_tight_fit_blue_tshirt_heartshirt\", \"acc_fit_turkeyhunter\", \"acc_fit_tuxleprechaun\", \"acc_fit_varsityjacket\", \"acc_fit_varsityjacket_black\", \"acc_fit_varsityjacket_gold\", \"acc_fit_varsityjacket_gold2\", \"acc_fit_varsityjacket_toasty\", \"acc_fit_viking\", \"acc_fit_viking_firestorm\", \"acc_fit_viking_flaxen\", \"acc_fit_viking_twilight\", \"acc_fit_warrior_ascendant\", \"acc_fit_warrior_ascendant_dark\", \"acc_fit_warrior_engineer\", \"acc_fit_warrior_scholar\", \"acc_fit_winterscarf\", \"acc_fit_worndownemployee\", \"acc_fit_worndownemployee_green\", \"acc_head_alienears\", \"acc_head_arbordaycrown\", \"acc_head_arbordaydruidhoodie\", \"acc_head_artisthat\", \"acc_head_banana_hat\", \"acc_head_beach_hat\", \"acc_head_beanie\", \"acc_head_beerhat\", \"acc_head_beret\", \"acc_head_beret_blue\", \"acc_head_beret_red\", \"acc_head_beret_yellow\", \"acc_head_black_1984_headphones\", \"acc_head_cap\", \"acc_head_catearscap\", \"acc_head_cathelmet\", \"acc_head_cathelmet_phoenix\", \"acc_head_chinesewarriorhelmet\", \"acc_head_chinesewarriorhelmet_gold\", \"acc_head_clownhat\", \"acc_head_coloredcap\", \"acc_head_coloredcap_fire\", \"acc_head_coloredcap_red\", \"acc_head_cone\", \"acc_head_cop\", \"acc_head_cowboy_hat\", \"acc_head_creatorcap\", \"acc_head_crochethat\", \"acc_head_crown\", \"acc_head_egghat\", \"acc_head_egghat_b\", \"acc_head_egghat_chocolate\", \"acc_head_egghat_golden\", \"acc_head_fedora_hat\", \"acc_head_frogeyes\", \"acc_head_goldenhalo\", \"acc_head_gopro\", \"acc_head_gopro_easter\", \"acc_head_goprojune\", \"acc_head_grapplesoldier_beret\", \"acc_head_grapplesoldier_beret_black\", \"acc_head_grapplesoldier_beret_blue\", \"acc_head_grapplesoldier_beret_red\", \"acc_head_grimreapercrown\", \"acc_head_hardhat\", \"acc_head_hardhat_canopy\", \"acc_head_hazmathelmet\", \"acc_head_hazmathelmet_blue\", \"acc_head_hazmathelmet_green\", \"acc_head_hazmathelmet_orange\", \"acc_head_hazmathelmet_pink\", \"acc_head_hazmathelmet_purple\", \"acc_head_hazmathelmet_red\", \"acc_head_horns\", \"acc_head_jesterhat\", \"acc_head_knifehat\", \"acc_head_kungfuhat\", \"acc_head_mage_hat\", \"acc_head_mexicanhat_redblack\", \"acc_head_mimic_hat\", \"acc_head_minerhat\", \"acc_head_minerhat_aura\", \"acc_head_minerhat_green\", \"acc_head_minerhat_red\", \"acc_head_mop\", \"acc_head_nflhelmet\", \"acc_head_nflhelmet_bear\", \"acc_head_nflhelmet_cat\", \"acc_head_nflhelmet_dog\", \"acc_head_nflhelmet_frog\", \"acc_head_nflhelmet_skeleton\", \"acc_head_parkranger\", \"acc_head_parkranger_car\", \"acc_head_parkranger_rugged\", \"acc_head_parkranger_salmon\", \"acc_head_partyhat\", \"acc_head_patriothat\", \"acc_head_pilgrimhat\", \"acc_head_pimp_hat\", \"acc_head_piratehat\", \"acc_head_piratehat_red\", \"acc_head_plunger\", \"acc_head_policehat\", \"acc_head_policehat_brown\", \"acc_head_propeller_cap\", \"acc_head_rainbow\", \"acc_head_rainbow_gold\", \"acc_head_rainbow_green\", \"acc_head_rainbow_ofdarkness\", \"acc_head_ricepattyhat\", \"acc_head_ricepattyhat_blue\", \"acc_head_securityguard\", \"acc_head_securityguard_green\", \"acc_head_sombrero\", \"acc_head_sombrero_crimson\", \"acc_head_sombrero_forest\", \"acc_head_sombrero_saffron\", \"acc_head_summerhat\", \"acc_head_summerhat_blue\", \"acc_head_summerhat_golden\", \"acc_head_summerhat_yellow\", \"acc_head_sweatband\", \"acc_head_tallcowboy_hat\", \"acc_head_tiara\", \"acc_head_tiara_gold\", \"acc_head_toilet_hat\", \"acc_head_top_hat\", \"acc_head_tophatclover\", \"acc_head_turkeyhat\", \"acc_head_turkeyhunter\", \"acc_head_vikinghelmet\", \"acc_head_vikinghelmet_firestorm\", \"acc_head_vikinghelmet_flaxen\", \"acc_head_vikinghelmet_twilight\", \"acc_head_winterglasses\", \"acc_head_winterhat\", \"acc_mask_arbordayshaman\", \"acc_mask_diademuertos\", \"acc_mask_hazmat\", \"acc_mask_hazmat_blue\", \"acc_mask_hazmat_green\", \"acc_mask_hazmat_orange\", \"acc_mask_hazmat_pink\", \"acc_mask_hazmat_purple\", \"acc_mask_hazmat_red\", \"acc_mask_jason\", \"acc_mask_medicalmask\", \"acc_mask_samuraimaskdemon\", \"acc_mask_samuraimaskdemon_purple\", \"acc_mask_samuraimaskdemon_red\", \"acc_mask_samuraimaskdemon_white\", \"acc_mask_squidgame\", \"acc_mask_squidgame_nut\", \"acc_mask_squidgame_star\", \"acc_mask_squidgamefrontman\", \"acc_mask_squidgamefrontman_gold\", \"acc_mouthcorner_lolipop\", \"acc_mouthcorner_lolipop_green\", \"acc_mouthcorner_rose\", \"acc_mouthcorner_tusks\", \"acc_mouthcorner_tusks_summon\", \"acc_nosetip_bunny\", \"acc_nosetip_bunny_blackwhite\", \"acc_nosetip_bunny_blue\", \"acc_nosetip_bunny_yellow\", \"acc_nosetip_clownnose\", \"acc_nosetip_steampunkmask\", \"acc_nosetip_steampunkmask_boat\", \"acc_nosetip_steampunkmask_fireengine\", \"acc_nosetip_steampunkmask_tinman\", \"animal_cat\", \"animal_chameleon\", \"animal_crab\", \"animal_cyborg_duck\", \"animal_duck\", \"animal_frog\", \"animal_germanshep\", \"animal_goat\", \"animal_gorilla\", \"animal_kitten\", \"animal_mole\", \"animal_polarbear\", \"animal_pug\", \"animal_rabbit\", \"animal_raccoon\", \"animal_reindeer\", \"animal_shark\", \"animal_shark_goblin\", \"animal_shark_hammer\", \"animal_skeletongorilla\", \"animal_tiger\", \"animal_trex\", \"animal_trex_shorthands\", \"animal_trex_winged\", \"animal_turkey\", \"animal_turtle\", \"bp_arm_l_cat\", \"bp_arm_l_chameleon\", \"bp_arm_l_crab\", \"bp_arm_l_demonarms\", \"bp_arm_l_duck\", \"bp_arm_l_duck_metal\", \"bp_arm_l_frog\", \"bp_arm_l_germanshep\", \"bp_arm_l_goat\", \"bp_arm_l_goldarms\", \"bp_arm_l_gorilla\", \"bp_arm_l_gorilla_og\", \"bp_arm_l_hookarms\", \"bp_arm_l_iceyarms\", \"bp_arm_l_kitten\", \"bp_arm_l_mole\", \"bp_arm_l_polarbear\", \"bp_arm_l_pug\", \"bp_arm_l_rabbit\", \"bp_arm_l_raccoon\", \"bp_arm_l_reindeer\", \"bp_arm_l_shark\", \"bp_arm_l_skeletongorilla\", \"bp_arm_l_slinkyarms\", \"bp_arm_l_tiger\", \"bp_arm_l_trex\", \"bp_arm_l_trex_short\", \"bp_arm_l_trex_wing\", \"bp_arm_l_turkey\", \"bp_arm_l_turtle\", \"bp_arm_r_cat\", \"bp_arm_r_chameleon\", \"bp_arm_r_crab\", \"bp_arm_r_demonarms\", \"bp_arm_r_duck\", \"bp_arm_r_duck_metal\", \"bp_arm_r_frog\", \"bp_arm_r_germanshep\", \"bp_arm_r_goat\", \"bp_arm_r_goldarms\", \"bp_arm_r_gorilla\", \"bp_arm_r_gorilla_og\", \"bp_arm_r_hookarms\", \"bp_arm_r_iceyarms\", \"bp_arm_r_kitten\", \"bp_arm_r_mole\", \"bp_arm_r_polarbear\", \"bp_arm_r_pug\", \"bp_arm_r_rabbit\", \"bp_arm_r_raccoon\", \"bp_arm_r_reindeer\", \"bp_arm_r_shark\", \"bp_arm_r_skeletongorilla\", \"bp_arm_r_slinkyarms\", \"bp_arm_r_tiger\", \"bp_arm_r_trex\", \"bp_arm_r_trex_short\", \"bp_arm_r_trex_wing\", \"bp_arm_r_turkey\", \"bp_arm_r_turtle\", \"bp_butt_bigbutt\", \"bp_butt_bigbutt_animals\", \"bp_butt_bigbutt_ducky\", \"bp_butt_bigbutt_galaxy\", \"bp_butt_bigbutt_golden\", \"bp_butt_bigbutt_hearts\", \"bp_butt_bigbutt_leaves\", \"bp_butt_cat\", \"bp_butt_chameleon\", \"bp_butt_crab\", \"bp_butt_duck\", \"bp_butt_frog\", \"bp_butt_germanshep\", \"bp_butt_goat\", \"bp_butt_gorilla\", \"bp_butt_kitten\", \"bp_butt_mole\", \"bp_butt_polarbear\", \"bp_butt_pug\", \"bp_butt_rabbit\", \"bp_butt_raccoon\", \"bp_butt_reindeer\", \"bp_butt_shark\", \"bp_butt_skeletongorilla\", \"bp_butt_tiger\", \"bp_butt_trex\", \"bp_butt_turkey\", \"bp_butt_turtle\", \"bp_eye_alieneyes\", \"bp_eye_buttoneyes\", \"bp_eye_cat\", \"bp_eye_chameleon\", \"bp_eye_crab\", \"bp_eye_demoneyes\", \"bp_eye_duck\", \"bp_eye_duck_cyborg\", \"bp_eye_frog\", \"bp_eye_frogeyes\", \"bp_eye_germanshep\", \"bp_eye_gloweyes\", \"bp_eye_goat\", \"bp_eye_goldeyes\", \"bp_eye_gorilla\", \"bp_eye_hearteyes\", \"bp_eye_kitten\", \"bp_eye_lenseyes\", \"bp_eye_lizardeyes\", \"bp_eye_mole\", \"bp_eye_ninjaeyes\", \"bp_eye_polarbear\", \"bp_eye_pug\", \"bp_eye_rabbit\", \"bp_eye_raccoon\", \"bp_eye_reindeer\", \"bp_eye_roboeyes\", \"bp_eye_shark\", \"bp_eye_skeletongorilla\", \"bp_eye_tiger\", \"bp_eye_trex\", \"bp_eye_turkey\", \"bp_eye_turtle\", \"bp_head_cat\", \"bp_head_chameleon\", \"bp_head_chameleon_crest\", \"bp_head_chameleon_horns\", \"bp_head_crab\", \"bp_head_duck\", \"bp_head_duck_cyborg\", \"bp_head_frog\", \"bp_head_germanshep\", \"bp_head_goat\", \"bp_head_goat_ramhorns\", \"bp_head_goat_shorthorns\", \"bp_head_gorilla\", \"bp_head_kitten\", \"bp_head_mole\", \"bp_head_polarbear\", \"bp_head_pug\", \"bp_head_rabbit\", \"bp_head_rabbit_foldedear\", \"bp_head_rabbit_lopear\", \"bp_head_raccoon\", \"bp_head_reindeer\", \"bp_head_shark\", \"bp_head_shark_goblin\", \"bp_head_shark_hammer\", \"bp_head_skeletongorilla\", \"bp_head_tiger\", \"bp_head_trex\", \"bp_head_turkey\", \"bp_head_turtle\", \"bp_tail_ankytail\", \"bp_tail_bananapeeltail\", \"bp_tail_cat\", \"bp_tail_chameleon\", \"bp_tail_donkeypintail\", \"bp_tail_duck\", \"bp_tail_electricalcordtail\", \"bp_tail_germanshep\", \"bp_tail_goat\", \"bp_tail_kitten\", \"bp_tail_mole\", \"bp_tail_polarbear\", \"bp_tail_pug\", \"bp_tail_rabbit\", \"bp_tail_raccoon\", \"bp_tail_reindeer\", \"bp_tail_shark\", \"bp_tail_tiger\", \"bp_tail_trex\", \"bp_tail_turkey\", \"bp_torso_cat\", \"bp_torso_chameleon\", \"bp_torso_crab\", \"bp_torso_duck\", \"bp_torso_frog\", \"bp_torso_germanshep\", \"bp_torso_goat\", \"bp_torso_gorilla\", \"bp_torso_kitten\", \"bp_torso_mole\", \"bp_torso_polarbear\", \"bp_torso_pug\", \"bp_torso_rabbit\", \"bp_torso_raccoon\", \"bp_torso_reindeer\", \"bp_torso_shark\", \"bp_torso_skeletongorilla\", \"bp_torso_tiger\", \"bp_torso_trex\", \"bp_torso_turkey\", \"bp_torso_turtle\", \"bp_torso_turtle_shell2\", \"bp_torso_turtle_shell3\", \"bp_torso_turtle_shell4\", \"character_battle_shark\", \"character_chame_leo\", \"character_delta_hare\", \"character_goat\", \"character_goat_ram\", \"character_goat_smallhorns\", \"character_grim_gorilla\", \"character_metal_duck\", \"character_mole_a_tov\", \"character_polar_paws\", \"character_shelllong\", \"character_sigma_frog\", \"character_swag_stag\", \"character_trex_pirate\", \"character_trex_pirate_crew\", \"character_turkey_hunter\", \"outfit_anime_fem_black\", \"outfit_anime_fem_pink\", \"outfit_anime_mas_blue\", \"outfit_anime_mas_white\", \"outfit_apocalypsesurvivor\", \"outfit_apocalypsesurvivor_banana\", \"outfit_apocalypsesurvivor_bloodorange\", \"outfit_apocalypsesurvivor_blueberry\", \"outfit_aquaarmor\", \"outfit_aquaarmor_green\", \"outfit_aquaarmor_red\", \"outfit_arborday_druid\", \"outfit_arborday_shaman\", \"outfit_arborday_tree\", \"outfit_armor_king\", \"outfit_bunny\", \"outfit_bunny_blackwhite\", \"outfit_bunny_blue\", \"outfit_bunny_yellow\", \"outfit_bunnydrip_blue\", \"outfit_bunnydrip_pink\", \"outfit_bunnydrip_yellow\", \"outfit_chinese_warrior\", \"outfit_chinese_warrior_gold\", \"outfit_cincodemayo\", \"outfit_cincodemayo_crimson\", \"outfit_cincodemayo_forest\", \"outfit_cincodemayo_saffron\", \"outfit_cincodemayoblanket\", \"outfit_cincodemayoblanket_crimson\", \"outfit_cincodemayoblanket_forest\", \"outfit_cincodemayoblanket_saffron\", \"outfit_clown\", \"outfit_cube\", \"outfit_cube_frog\", \"outfit_cube_gorilla\", \"outfit_cube_shepherd\", \"outfit_cupid\", \"outfit_cybersuit\", \"outfit_cyborg_punk\", \"outfit_deltahare_blue\", \"outfit_deltahare_desert\", \"outfit_deltahare_green\", \"outfit_deltahare_snow\", \"outfit_demolitionjumpsuit\", \"outfit_demolitionjumpsuit_green\", \"outfit_demolitionjumpsuit_red\", \"outfit_demonboyband\", \"outfit_demonboyband_glowblue\", \"outfit_demonboyband_glowgreen\", \"outfit_demonboyband_glowpurple\", \"outfit_discobutt\", \"outfit_discobutt_phoenix\", \"outfit_diversuit\", \"outfit_diversuit_green\", \"outfit_diversuit_rusty\", \"outfit_diversuit_yellow\", \"outfit_dwarf\", \"outfit_dwarf_blue\", \"outfit_dwarf_tin\", \"outfit_dwarf_wood\", \"outfit_eggsuit_chocolate\", \"outfit_eggsuit_colorful_green\", \"outfit_eggsuit_colorful_purple\", \"outfit_eggsuit_golden\", \"outfit_elf_blue\", \"outfit_elf_green\", \"outfit_elf_pink\", \"outfit_employee_suit_blue\", \"outfit_employee_suit_gold\", \"outfit_employee_suit_purple\", \"outfit_fallponcho\", \"outfit_fur_future\", \"outfit_gladiator\", \"outfit_gladiator_cat\", \"outfit_gladiator_frog\", \"outfit_gladiator_gorilla\", \"outfit_gladiator_pug\", \"outfit_gladiator_skeletongorilla\", \"outfit_glowgrilla\", \"outfit_glowgrilla_purple\", \"outfit_grapplesoldier\", \"outfit_grapplesoldier_black\", \"outfit_grapplesoldier_blue\", \"outfit_grapplesoldier_red\", \"outfit_grimreaper_premium\", \"outfit_hawaiian\", \"outfit_hawaiian_blue\", \"outfit_hawaiian_yellow\", \"outfit_hawaiiangirl\", \"outfit_hawaiiangirl_blonde\", \"outfit_hawaiiangirl_brown\", \"outfit_hazmat_blue\", \"outfit_hazmat_green\", \"outfit_hazmat_orange\", \"outfit_hazmat_pink\", \"outfit_hazmat_purple\", \"outfit_hazmat_red\", \"outfit_hazmat_yellow\", \"outfit_hippie\", \"outfit_irish_kilt\", \"outfit_irish_kilt_blue\", \"outfit_irish_kilt_red\", \"outfit_irish_kilt_yellow\", \"outfit_it_employee_blue\", \"outfit_it_employee_brown\", \"outfit_kingofhearts_blue\", \"outfit_kingofhearts_red\", \"outfit_kpop\", \"outfit_kpop_black\", \"outfit_kpop_purple\", \"outfit_kpop_white\", \"outfit_kungfu_black\", \"outfit_kungfu_blue\", \"outfit_kungfu_orange\", \"outfit_leprachaun\", \"outfit_liona\", \"outfit_necromancer\", \"outfit_neon_miner\", \"outfit_nfljersey_bear\", \"outfit_nfljersey_cat\", \"outfit_nfljersey_frog\", \"outfit_nfljersey_gorilla\", \"outfit_nfljersey_pug\", \"outfit_nfljersey_skeleton\", \"outfit_og_fit1\", \"outfit_og_fit2\", \"outfit_orcmage\", \"outfit_orcmage_summon\", \"outfit_parkranger\", \"outfit_parkranger_car\", \"outfit_parkranger_rugged\", \"outfit_parkranger_salmon\", \"outfit_pilgrim\", \"outfit_pirate_blue\", \"outfit_pirate_crew\", \"outfit_pirate_red\", \"outfit_policeman_blue\", \"outfit_policeman_brown\", \"outfit_potofgold\", \"outfit_potofgold_flames\", \"outfit_potofgold_gold\", \"outfit_potofgold_green\", \"outfit_punkrock\", \"outfit_queenofhearts\", \"outfit_racerjacket_black\", \"outfit_racerjacket_red\", \"outfit_racerjacket_white\", \"outfit_racerjacket_yellow\", \"outfit_redknight\", \"outfit_redknight_summon\", \"outfit_rocker\", \"outfit_samurai\", \"outfit_samurai_purple\", \"outfit_samurai_red\", \"outfit_samurai_white\", \"outfit_samuraiwarrior\", \"outfit_samuraiwarrior_dual\", \"outfit_samuraiwarrior_orange\", \"outfit_samuraiwarrior_pink\", \"outfit_santa\", \"outfit_santa_blue\", \"outfit_santa_purple\", \"outfit_securityguard_green\", \"outfit_securityguard_white\", \"outfit_shiny_swim_set\", \"outfit_spacesuit\", \"outfit_spacesuit_blue\", \"outfit_spacesuit_orange\", \"outfit_spacesuit_rainbow\", \"outfit_squidgame_pink\", \"outfit_squidgame_purple\", \"outfit_squidgame_red\", \"outfit_squidgamedoll\", \"outfit_squidgamedoll_brunette\", \"outfit_squidgamefrontman\", \"outfit_squidgamefrontman_white\", \"outfit_steampunkrobot\", \"outfit_steampunkrobot_boat\", \"outfit_steampunkrobot_fireengine\", \"outfit_steampunkrobot_tinman\", \"outfit_supermansuit\", \"outfit_supermansuit_atom\", \"outfit_supermansuit_leaf\", \"outfit_supermansuit_recycle\", \"outfit_tacticalarmor\", \"outfit_tacticalarmor_emo\", \"outfit_tacticalarmor_pale\", \"outfit_tacticalarmor_robo\", \"outfit_tacticalarmor_robo_copper\", \"outfit_tacticalmining\", \"outfit_tacticalmining_almandine\", \"outfit_tacticalmining_diamond\", \"outfit_tacticalmining_emerald\", \"outfit_teamblue\", \"outfit_teamblue_fire\", \"outfit_teamred\", \"outfit_thanksgiving_turkey\", \"outfit_trek\", \"outfit_valentines_suit\", \"outfit_valentines_youme\", \"outfit_viking\", \"outfit_viking_firestorm\", \"outfit_viking_flaxen\", \"outfit_viking_twilight\", \"outfit_warrior_ascendant\", \"outfit_warrior_ascendant_dark\", \"outfit_warrior_engineer\", \"outfit_warrior_scholar\", \"outfit_worndownemployee_blue\", \"outfit_worndownemployee_green\"]}",
        "version": "277a87beb4905dbe2333d5cd55a7e5be",
        "permission_read": 1,
        "create_time": "2024-09-20T21:26:18Z",
        "update_time": "2025-08-07T01:22:02Z"
        },
        {
        "collection": "user_inventory",
        "key": "research",
        "user_id": "3560fe2e-015c-4d2b-b2a6-6eb9f8d6a236",
        "value": "{\"nodes\": [\"node_dynamite\", \"node_teleport_grenade\", \"node_glowsticks\", \"node_skill_backpack_cap_1\", \"node_skill_health_1\", \"node_crowbar\", \"node_flaregun\", \"node_ogre_hands\", \"node_revolver\", \"node_skill_gundamage_1\", \"node_skill_explosive_1\", \"node_rpg\", \"node_skill_selling_1\", \"node_revolver_ammo\", \"node_rpg_ammo\", \"node_flashbang\", \"node_impact_grenade\", \"node_cluster_grenade\", \"node_jetpack\", \"node_shotgun\", \"node_tripwire_explosive\", \"node_crossbow\", \"node_tablet\", \"node_plunger\", \"node_umbrella\", \"node_backpack\", \"node_flashlight_mega\", \"node_lance\", \"node_balloon\", \"node_saddle\", \"node_skill_right_hip_attachment\", \"node_skill_left_hip_attachment\", \"node_sticky_dynamite\", \"node_rpg_cny\", \"node_zipline_gun\", \"node_zipline_rope\", \"node_company_ration\", \"node_balloon_heart\", \"node_crossbow_heart\", \"node_arrow\", \"node_arrow_heart\", \"node_hoverpad\", \"node_quiver\", \"node_backpack_large\", \"node_shield\", \"node_shield_police\", \"node_hookshot\", \"node_baseball_bat\", \"node_police_baton\", \"node_heart_gun\", \"node_pogostick\", \"node_boxfan\", \"node_mega_broccoli\", \"node_mini_broccoli\", \"node_dynamite_cube\", \"node_skill_backpack_cap_2\", \"node_whoopie\", \"node_disposable_camera\", \"node_sticker_dispenser\", \"node_impulse_grenade\", \"node_stash_grenade\", \"node_cardboardbox\", \"node_rpg_easter\", \"node_rpg_ammo_egg\", \"node_pinata_bat\", \"node_hawaiian_drum\", \"node_ukulele\", \"node_anti_gravity_grenade\", \"node_antigrav_grenade\", \"node_football\", \"node_skill_backpack_cap_3\", \"node_item_nut_shredder\", \"node_hookshot_sword\", \"node_rpg_spear\", \"node_rpg_ammo_spear\", \"node_skill_health_2\", \"node_skill_selling_2\", \"node_skill_selling_3\", \"node_frying_pan\", \"node_skill_melee_1\", \"node_skill_melee_2\", \"node_skill_melee_3\", \"node_viking_hammer\", \"node_viking_hammer_twilight\", \"node_mega_broccoli_bomb\", \"node_micro_broccoli_bomb\", \"node_teleport_gun\", \"node_arrow_bomb\", \"node_robo_monke\", \"node_friend_launcher\", \"node_grenade_launcher\"]}",
        "version": "58c1d1c4ade0e8e205939be8a07ce49b",
        "permission_read": 1,
        "create_time": "2024-11-25T17:55:33Z",
        "update_time": "2025-07-14T21:34:27Z"
        },
        {
        "collection": "user_inventory",
        "key": "stash",
        "user_id": "3560fe2e-015c-4d2b-b2a6-6eb9f8d6a236",
        "value": "{\"items\": []}",
        "version": "d1315c03b540bef68ce4742d46e77cc0",
        "permission_read": 1,
        "permission_write": 1,
        "create_time": "2025-02-11T22:35:00Z",
        "update_time": "2025-08-07T17:14:27Z"
        },
        {
        "collection": "user_inventory",
        "key": "stash_upgrades",
        "user_id": "3560fe2e-015c-4d2b-b2a6-6eb9f8d6a236",
        "value": "{\"upgrades\": [\"col_1\", \"col_2\", \"col_3\", \"col_4\", \"col_5\", \"col_6\", \"col_7\", \"col_8\", \"row_1\", \"row_2\", \"row_3\", \"row_4\", \"row_5\", \"row_6\", \"row_7\", \"row_8\", \"mtl_1\", \"mtl_2\", \"mtl_3\", \"mtl_4\", \"mtl_5\", \"mtl_6\", \"mtl_7\", \"mtl_8\"]}",
        "version": "af1feb89bd8c849f5f16a4754577be04",
        "permission_read": 1,
        "create_time": "2025-07-23T23:32:02Z",
        "update_time": "2025-08-07T17:05:15Z"
        },
        {
        "collection": "user_inventory",
        "key": "gameplay_loadout",
        "user_id": "3560fe2e-015c-4d2b-b2a6-6eb9f8d6a236",
        "value": "{\"version\": 1}",
        "version": "3846efa925d304495efbfed41eaafe74",
        "permission_read": 1,
        "permission_write": 1,
        "create_time": "2024-10-30T01:21:34Z",
        "update_time": "2025-08-08T20:34:56Z"
        },
        {
        "collection": "user_preferences",
        "key": "gameplay_items",
        "user_id": "3560fe2e-015c-4d2b-b2a6-6eb9f8d6a236",
        "value": "{\"recents\": []}",
        "version": "fe9acf47fd31aeb3ea1aa209e6485ce3",
        "permission_read": 1,
        "permission_write": 1,
        "create_time": "2024-12-10T20:44:21Z",
        "update_time": "2025-08-09T07:39:43Z"
        },
        {
        "collection": "user_preferences",
        "key": "common",
        "user_id": "3560fe2e-015c-4d2b-b2a6-6eb9f8d6a236",
        "value": "{\"appearOffline\": false}",
        "version": "d56295314bb7a4c43e13da9c446a77a8",
        "permission_read": 1,
        "permission_write": 1,
        "create_time": "2025-06-11T03:57:33Z",
        "update_time": "2025-08-07T18:09:40Z"
        }
    ]
    }

@app.route('/3/v2/rpc/purchase.list', methods=['GET'])
@app.route('/v2/rpc/purchase.list', methods=['GET'])
@app.route('/nnnnaakamacloud.c/v2/rpc/purchase.list', methods=['GET'])
def purchaselist():
    return {
        "payload": "{\"purchases\":[{\"user_id\":\"3560fe2e-015c-4d2b-b2a6-6eb9f8d6a236\",\"product_id\":\"KPOP_GOLD\",\"transaction_id\":\"716802304855579\",\"store\":3,\"purchase_time\":{\"seconds\":1754458259},\"create_time\":{\"seconds\":1754458305,\"nanos\":154543000},\"update_time\":{\"seconds\":1754458305,\"nanos\":154543000},\"refund_time\":{},\"provider_response\":\"{\\\"success\\\": true, \\\"grant_time\\\": 1754458259}\",\"environment\":2},{\"user_id\":\"3560fe2e-015c-4d2b-b2a6-6eb9f8d6a236\",\"product_id\":\"CHAMELEON_BUNDLE\",\"transaction_id\":\"642819158920561\",\"store\":3,\"purchase_time\":{\"seconds\":1748315321},\"create_time\":{\"seconds\":1748315350,\"nanos\":615822000},\"update_time\":{\"seconds\":1748315350,\"nanos\":615822000},\"refund_time\":{},\"provider_response\":\"{\\\"success\\\": true, \\\"grant_time\\\": 1748315321}\",\"environment\":2},{\"user_id\":\"3560fe2e-015c-4d2b-b2a6-6eb9f8d6a236\",\"product_id\":\"SHELLLONG_BUNDLE\",\"transaction_id\":\"583001341569010\",\"store\":3,\"purchase_time\":{\"seconds\":1742932724},\"create_time\":{\"seconds\":1742932880,\"nanos\":773282000},\"update_time\":{\"seconds\":1742932880,\"nanos\":773282000},\"refund_time\":{},\"provider_response\":\"{\\\"success\\\": true}\",\"environment\":2},{\"user_id\":\"3560fe2e-015c-4d2b-b2a6-6eb9f8d6a236\",\"product_id\":\"G.O.A.T_BUNDLE\",\"transaction_id\":\"556928314176313\",\"store\":3,\"purchase_time\":{\"seconds\":1740523561},\"create_time\":{\"seconds\":1740523626,\"nanos\":858485000},\"update_time\":{\"seconds\":1741616276,\"nanos\":636221000},\"refund_time\":{},\"provider_response\":\"{\\\"success\\\": true}\",\"environment\":2},{\"user_id\":\"3560fe2e-015c-4d2b-b2a6-6eb9f8d6a236\",\"product_id\":\"CURRENCY_SMALL\",\"transaction_id\":\"520077871194691\",\"store\":3,\"purchase_time\":{\"seconds\":1737165591},\"create_time\":{\"seconds\":1737165616,\"nanos\":219758000},\"update_time\":{\"seconds\":1737165616,\"nanos\":219758000},\"refund_time\":{},\"provider_response\":\"{\\\"success\\\": true}\",\"environment\":2},{\"user_id\":\"3560fe2e-015c-4d2b-b2a6-6eb9f8d6a236\",\"product_id\":\"POLAR_PAWS_BUNDLE\",\"transaction_id\":\"498846086651203\",\"store\":3,\"purchase_time\":{\"seconds\":1735139449},\"create_time\":{\"seconds\":1735155215,\"nanos\":988535000},\"update_time\":{\"seconds\":1735155215,\"nanos\":988535000},\"refund_time\":{},\"provider_response\":\"{\\\"success\\\": true}\",\"environment\":2},{\"user_id\":\"3560fe2e-015c-4d2b-b2a6-6eb9f8d6a236\",\"product_id\":\"FROG_BUNDLE\",\"transaction_id\":\"411070858762060\",\"store\":3,\"purchase_time\":{\"seconds\":1726952768},\"create_time\":{\"seconds\":1726953016,\"nanos\":937191000},\"update_time\":{\"seconds\":1726953016,\"nanos\":937191000},\"refund_time\":{},\"provider_response\":\"{\\\"success\\\": true}\",\"environment\":2}]}"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7080)

