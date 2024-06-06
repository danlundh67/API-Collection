#!/usr/bin/env python3

from tuyapy import TuyaApi

USERNAME = 'cbjelke@gmail.com' # username (email) from the android app

PASSWORD = 'FHC-22/23' # password you set in your android app - choose a random one :)

COUNTRY_CODE = '46' # make sure you choose your country when registering in the app

api = TuyaApi()

api.init(USERNAME, PASSWORD, COUNTRY_CODE)

for device in api.get_all_devices():
    print(device.object_id())
