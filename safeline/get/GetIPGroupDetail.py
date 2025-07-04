import requests
import json


class GetIPGroupDetail:
    def __init__(self, host: str, token: str):
        self.url = host + "/api/open/ipgroup/detail"
        self.headers = {
            "X-SLCE-API-TOKEN": token
        }

    def get(self, group_id: int):
        _url = self.url + "?id=" + str(group_id)
        res = requests.get(url=_url, headers=self.headers, verify=False)
        # 返回 IP组 data 数据
        return res.json()["data"].get("data", {})
