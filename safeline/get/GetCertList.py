import requests
import json


class GetCertList:
    def __init__(self, host, token):
        self.url = host + "/api/open/cert"
        self.header = {
            "X-SLCE-API-TOKEN": token
        }

    def get(self):
        res = requests.get(url=self.url, headers=self.header, verify=False)
        print("当前证书列表:")
        print(json.dumps(res.json(), ensure_ascii=False, indent=4))
