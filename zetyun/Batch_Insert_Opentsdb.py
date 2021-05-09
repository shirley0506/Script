#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import random
import requests


def send_json(json, s):
    result = s.post("http://172.20.3.122:4242/api/put?details", json=json)
    return result.text


'''
指标数据：实时写入

def main():
    s = requests.session()
    # a = int(time.time()*1000)
    ls = []
    for i in range(1, 101):
        json = {
            "metric": "xuqq_real_time",
            "timestamp": int(time.time()*1000),
            "value": random.randint(0, 1000),
            "tags": {
                "host": "172.20.3.120"
            }
        }
        send_json(json, s)
        time.sleep(60)
        i += 1
        ls.append(json)

    with open('metric.txt', 'a') as f:
        f.write(str(ls))

'''

'''
批量写入指标数据
'''

def main():
    s = requests.Session()
    a = int(time.time() * 1000) - 4*24*60*60*1000
    ls = []
    for i in range(1, 61):
        json = {
            "metric": "xuqq_real_time",
            "timestamp": a,
            "value": random.randint(0, 1000),
            "tags": {
                "host": "172.20.3.120",
            }
        }
        i += 1
        a += 60000
        with open('metric.txt', 'a') as f:
            f.write(str(json) + '\n')
        ls.append(json)
        if len(ls) >= 50:
            send_json(ls, s)
            ls = []
    send_json(ls, s)
    # ls = []




if __name__ == "__main__":
    main()
