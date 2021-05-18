#!/usr/bin/python3
# -*- coding: utf-8 -*-
import datetime
import time
import random
import requests
from datetime import datetime as dt


def send_json(json, s):
    result = s.post("http://172.20.3.122:4242/api/put?details", json=json)
    print(result.text)


def assign_timestamp(month=dt.now().month, day=dt.now().day, hour=dt.now().hour, minute=dt.now().minute):
    '''
    指定时间转成时间戳
    :param month:
    :param day:
    :param hour:
    :param minute:
    :return:
    '''
    assign_date = datetime.date(year=2021, month=month, day=day)
    assign_time = datetime.time(hour=hour, minute=minute, second=random.randint(1, 59),
                                microsecond=random.randint(1, 1000001))
    a = int(datetime.datetime.combine(date=assign_date, time=assign_time).timestamp() * 1000)
    return a


'''
指标数据：实时写入
'''


def current(metric_name, IP, s):
    ls = []
    while True:
        for ip in IP:
            json = {
                "metric": metric_name,
                "timestamp": int(time.time() * 1000),
                # "value": random.randint(1, 600),
                "value": 60,
                "tags": {
                    "host": ip
                }
            }
            ls.append(json)
            with open('metric.txt', 'a') as f:
                f.write(str(json) + '\n')
        send_json(ls, s)
        time.sleep(60)
        ls = []


'''
批量写入指标数据
'''


def batch(a, metric_name, s, value_min, value_max):
    # s = requests.Session()
    ls = []
    for i in range(1, 61):
        for ip in IP:
            # 多序列指标
            json = {
                "metric": metric_name,
                "timestamp": a,
                # "timestamp": int(time.time() * 1000),
                "value": random.randint(value_min, value_max),
                "tags": {
                    "host": ip
                }
            }
            ls.append(json)
            with open('metric.txt', 'a') as f:
                f.write(str(json) + '\n')
        send_json(ls, s)
        i += 1
        a -= 60000


if __name__ == "__main__":
    s = requests.session()
    variable_parameter = []
    metric_name = 'xuqq_specialDay_9'
    IP = ['172.20.3.120', '172.20.3.121', '172.20.3.122']
    # 批量写指标数据
    # last_day = 7
    # early_day = 7
    # b = random.randint(1, 100)
    # print(str(last_day) + "至" + str(early_day) + "日最大值：" + str(b+100) + ",最小值：" + str(b))
    # for i in range(early_day, last_day+1):
    #     variable_parameter.append([])
    #     # b = random.randint(1, 100)
    #     variable_parameter[i - early_day].append(i)
    #     variable_parameter[i - early_day].append(b)
    #     variable_parameter[i - early_day].append(b + 100)
    # for i in range(len(variable_parameter)):
    #     day = variable_parameter[i][0]
    #     value_min = variable_parameter[i][1]
    #     value_max = variable_parameter[i][2]
    #     variable = {'month': 5, 'day': day, 'hour': 10, 'minute': 0}
    #     past_timestamp = assign_timestamp(**variable)
    #     batch(past_timestamp, metric_name, s, value_min, value_max)
    # # 写实时日志
    current(metric_name, IP, s)

