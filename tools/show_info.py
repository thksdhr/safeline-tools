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
# endregion

# 获取信息
GetList = GetIPGGroupList(HOST, TOKEN)
GetList.get()
