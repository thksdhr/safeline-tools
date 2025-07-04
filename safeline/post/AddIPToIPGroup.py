import requests
import json


class AddIPToIPGroup:
    def __init__(self, host: str, token: str):
        self.url = host + "/api/open/ipgroup/append"
        self.header = {
            "X-SLCE-API-TOKEN": token
        }
        self.parameters = {
            "ip_group_ids": [
                3
            ],
            "ips": [
            ]
        }

    def add(self):
        ip_list_str = requests.get("https://ispip.clang.cn/all_cn.txt").text
        ip_list = ip_list_str.splitlines()
        print("最新IP池大小:", len(ip_list))
        for ip in ip_list:
            self.parameters["ips"].append(ip)
        # print(json.dumps(self.parameters, indent=4))
        requests.post(url=self.url, headers=self.header, data=json.dumps(self.parameters, ensure_ascii=False),
                      verify=False)
