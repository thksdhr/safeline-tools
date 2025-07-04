import requests
import os
import json


def get_ips(url: str, debug: bool = False):
    print("开始获取IP订阅，订阅URL：" + url)
    res = requests.get(url)
    ips = res.text.splitlines()
    print("获取订阅成功，IP数量=" + str(len(ips)))
    if debug:
        print(ips)
    return ips


def get_cert(url: str, debug: bool = False):
    print("获取URL:" + url)
    res = requests.get(url)
    _data = res.text
    print("获取数据成功~")
    if debug:
        print(_data)
    return _data
