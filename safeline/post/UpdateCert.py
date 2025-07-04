import requests
import json


class UpdateCert:
    def __init__(self, host, token):
        self.url = host + "/api/open/cert"
        self.header = {
            "X-SLCE-API-TOKEN": token
        }

    def update(self, cert_id: int, cert_type: int, crt: str, key: str):
        _data = {
            "id": cert_id,
            "type": cert_type,
            "manual": {
                "crt": crt,
                "key": key
            }
        }
        res = requests.post(url=self.url, headers=self.header, data=json.dumps(_data), verify=False)
        print(json.dumps(res.json(), ensure_ascii=False, indent=4))
