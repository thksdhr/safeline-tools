import json

import Tools
from safeline import *
import os
from urllib3.exceptions import InsecureRequestWarning

# region 初始化
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
config_file_path = "../config.json"
if os.path.exists(config_file_path):
    print("配置文件存在")
    with open(config_file_path, "r") as f:
        print(json.dumps(json.load(f), ensure_ascii=False, indent=4))
    print("初始化完成！")
else:
    raise Exception("配置文件不存在！？请创建配置文件！！！")
with open("../config.json", "r", encoding="utf-8") as f:
    CFG = json.load(f)
TOKEN = CFG["Token"]
HOST = CFG["Host"]
UpdateList = CFG["UpdateIPGroup"]
if TOKEN == '' or HOST == '' or len(UpdateList) == 0:
    raise Exception("无法解析配置文件！！！请正确填写配置文件！！！")
# endregion

group_detail = GetIPGroupDetail(HOST, TOKEN)
update_group = UpdateIPGroup(HOST, TOKEN)
for f in UpdateList:
    print("IP组ID=" + str(f.get("GroupID")))
    print("IP组更新Url地址=" + str(f.get("Url")))
    _data = group_detail.get(f.get("GroupID"))
    _ips = Tools.get_ips(f.get("Url"))
    _data["ips"] = _ips
    update_group.update(_data)

# 更新IP组
