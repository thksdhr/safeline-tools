import requests
import json


class UpdateIPGroup:
    def __init__(self, host: str, token: str):
        self.url = host + "/api/open/ipgroup"
        self.header = {
            "X-SLCE-API-TOKEN": token
        }

    def update(self, data: {}):
        res = requests.put(url=self.url, headers=self.header, data=json.dumps(data), verify=False)
        print(json.dumps(res.json(), indent=4))

    def update_ips(self, group_id: int, ips: []):
        _data = {
            "id": group_id,
            "ips": ips
        }
        res = requests.put(url=self.url, headers=self.header, data=json.dumps(_data), verify=False)
        print(json.dumps(res.json(), indent=4))
