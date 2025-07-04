# region 加载模块
import json
import argparse
import os
import requests
# disable SSL warnings
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
# load safeline api
from safeline import *
import Tools

# endregion

# region load config
with open("config.json", "r", encoding="utf-8") as f:
    CFG = json.load(f)
TOKEN = CFG["Token"]
HOST = CFG["Host"]

# endregion

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="safeline-tools",
                                     description="这是一个简单的小程序，使用了雷池官方API实现了更新雷池IP组和证书的功能~",
                                     epilog="by:taoziG")
    # 添加参数
    parser.add_argument("-configs", type=str, default="./config.json", help="配置文件路径~")
    parser.add_argument("-v", action="store_true", help="显示详细信息。")
    parser.add_argument("-info", action="store_true", help="获取雷池的详细信息。")
    parser.add_argument("-ipgroup", action="store_true", help="更新IP组。")
    parser.add_argument("-certs", action="store_true", help="更新证书。")

    # 解析参数
    args = parser.parse_args()

    # region 加载配置
    if os.path.exists(args.configs):
        print("读取配置文件...")
        with open(args.configs, "r", encoding="utf-8") as f:
            _config = json.load(f)
            if args.v:
                print(json.dumps(_config, indent=4, ensure_ascii=False))
        print("配置文件加载完成...")
    else:
        raise Exception("配置文件" + args.configs + "不存在！？请创建配置文件！！！")
    _token = _config["Token"]
    _host = _config["Host"]
    # endregion

    # 获取雷池信息
    if args.info:
        print("获取雷池当前所有IP组信息:")
        getIPGroupList = GetIPGGroupList(host=_host, token=_token)
        getIPGroupList.get()
        print("获取雷池当前所有证书信息:")
        _getCertList = GetCertList(host=_host, token=_token)
        _getCertList.get()

    #region 更新IP组
    if args.ipgroup:
        print("开始更新IP组订阅...")
        _ipGroupList = _config["UpdateIPGroup"]
        ipGroupDetail = GetIPGroupDetail(host=_host, token=_token)
        ipGroupUpdate = UpdateIPGroup(host=_host, token=_token)
        for i in _ipGroupList:
            print("IP组ID=" + str(i.get("GroupID")))
            print("IP组更新Url地址=" + str(i.get("Url")))
            _data = ipGroupDetail.get(i.get("GroupID"))
            _ips = requests.get(i.get("Url")).text.splitlines()
            print("获取订阅成功，IP数量=" + str(len(_ips)))
            _data["ips"] = _ips
            ipGroupUpdate.update(_data)
        print("IP组订阅更新完成.")
    #endregion

    # region 更新SSL证书
    if args.certs:
        print("开始更新SSL证书...")
        _certList = _config["UpdateCerts"]
        certUpdate = UpdateCert(host=_host, token=_token)
        for i in _certList:
            print("SSL证书ID=" + str(i.get("CertID")))
            print("SSL证书Type=" + str(i.get("CertType")))
            print("SSL证书公钥URL=" + str(i.get("PublicKeyUrl")))
            print("SSL证书私钥URL=" + str(i.get("PrivateKeyUrl")))
            _publicKey = requests.get(i.get("PublicKeyUrl")).text
            _privateKey = requests.get(i.get("PrivateKeyUrl")).text
            certUpdate.update(cert_id=i.get("CertID"), cert_type=i.get("CertType"), crt=_publicKey, key=_privateKey)
        print("证书更新完成.")
    # endregion
