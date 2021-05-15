#!/usr/bin/python3
# -*- coding: utf-8 -*-
import datetime
import time
import random
import requests


def send_json(json, s):
    result = s.post("http://172.20.3.122:4242/api/put?details", json=json)
    print(result.text)


def assign_timestamp(month, day, hour, minute):
    '''
    指定时间转成时间戳
    :param month:
    :param day:
    :param hour:
    :param minute:
    :return:
    '''
    assign_date = datetime.date(year=2021, month=month, day=day)
    assign_time = datetime.time(hour=hour, minute=minute, second=random.randint(1, 61),
                                microsecond=random.randint(1, 1000001))
    a = int(datetime.datetime.combine(date=assign_date, time=assign_time).timestamp()*1000)
    return a



IP = ['172.20.3.120', '172.20.3.121', '172.20.3.122']

'''
指标数据：实时写入
'''


def current():
    s = requests.session()
    ls = []
    while True:
        for ip in IP:
            json = {
                "metric": "xuqq_tread_null_anomaly",
                "timestamp": int(time.time() * 1000),
                "value": random.randint(500, 601),
                "tags": {
                    "host": ip
                }
            }
            ls.append(json)
        send_json(json, s)
        with open('metric.txt', 'a') as f:
            f.write(str(json))
        time.sleep(60)
        ls = []


'''
批量写入指标数据
'''


def batch(a):
    s = requests.Session()
    ls = []
    for i in range(1, 61):
        for ip in IP:
            # 多序列指标
            json = {
                "metric": "xuqq_specialDay",
                "timestamp": a,
                # "timestamp": int(time.time() * 1000),
                "value": random.randint(500, 601),
                "tags": {
                    "host": ip
                }
            }
            ls.append(json)
            with open('metric.txt', 'a') as f:
                f.write(str(json) + '\n')
        # send_json(ls, s)
        i += 1
        a -= 60000


if __name__ == "__main__":
    variable = {'month': 5, 'day': 14, 'hour': 10, 'minute': 30}
    past_timestamp = assign_timestamp(**variable)
    batch(past_timestamp)
