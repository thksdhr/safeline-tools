import requests
import json


class GetIPGGroupList:

    def __init__(self, host: str, token: str):
        self.url = host + "/api/open/ipgroup"
        self.header = {
            "X-SLCE-API-TOKEN": token
        }

    def get(self, top: int = 0):
        if top != 0:
            _url = self.url + "?top=" + str(top)
        else:
            _url = self.url
        res = requests.get(url=_url, headers=self.header, verify=False)
        print(json.dumps(res.json(), ensure_ascii=False, indent=4))
        return res
