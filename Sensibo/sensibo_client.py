import requests
import json

# 
# 
# all script with 
# sensibo_client.py 'your apikey' 'your device name'

_SERVER = 'https://home.sensibo.com/api/v2'

class SensiboClientAPI(object):
    def __init__(self, api_key):
        self._api_key = api_key

    def _get(self, path, ** params):
        params['apiKey'] = self._api_key
        response = requests.get(_SERVER + path, params = params)
        response.raise_for_status()
        return response.json()

    def _patch(self, path, data, ** params):
        params['apiKey'] = self._api_key
        response = requests.patch(_SERVER + path, params = params, data = data)
        response.raise_for_status()
        return response.json()

    def devices(self):
        result = self._get("/users/me/pods", fields="id,room")
        return {x['room']['name']: x['id'] for x in result['result']}

    def pod_measurement(self, podUid):
        result = self._get("/pods/%s/measurements" % podUid)
        #print(result,podUid)
        return result['result']

    def pod_ac_state(self, podUid):
        result = self._get("/pods/%s/acStates" % podUid, limit = 1, fields="acState")
        return result['result'][0]['acState']

    def pod_change_ac_state(self, podUid, currentAcState, propertyToChange, newValue):
        self._patch("/pods/%s/acStates/%s" % (podUid, propertyToChange),
                json.dumps({'currentAcState': currentAcState, 'newValue': newValue}))

    def pod_ac_timer(self, podUid):
        result = self._get("/pods/%s/timer/ " % podUid)
        return result


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Sensibo client example parser')
    parser.add_argument('apikey', type = str)
    parser.add_argument('deviceName', type = str)
    args = parser.parse_args()

    client = SensiboClientAPI(args.apikey)
    devices = client.devices()
    print("----------", "devices", "----------")
    print(devices)

    uid = devices[args.deviceName]
    ac_state = client.pod_ac_state(uid)
    ac_temp=client.pod_measurement(uid)
    #ac_timer = client.pod_ac_timer(uid)
    
    print ("-" * 10, "AC State of %s" % args.deviceName, "-" * 10)
    print(ac_state)
    print(ac_temp)

    # client.pod_change_ac_state(uid, ac_state, "on", not ac_state['on'])
