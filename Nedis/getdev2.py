import requests
import pprint
import time

print("GET AUTH-TOKEN")
auth = requests.post(
    "https://px1.tuyaus.com/homeassistant/auth.do",
    data={
        "userName": "cbjelke@gmail.com",
        "password": "FHC-22/23",
        "countryCode": "46",
        "bizType": "tuya",
        "from": "tuya",
    },
).json()
pprint.pprint(auth)
access_token = auth["access_token"]
print(">> ACCESS_TOKEN=" + access_token)

print("GET DEVICES")
devices = requests.post(
    "https://px1.tuyaus.com/homeassistant/skill",
    json={"header": {"name": "Discovery", "namespace": "discovery", "payloadVersion": 1}, "payload": {"accessToken": access_token}}
).json()
pprint.pprint(devices)
bell_device = next(dev for dev in devices["payload"]["devices"] if "bell" in dev["name"])
bell_id = bell_device["id"]
print(">> BELL_ID=" + bell_id)
