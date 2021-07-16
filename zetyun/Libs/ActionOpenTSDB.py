#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @FileName: ActionOpenTSDB.py
# @Time: 2021/7/9 4:58 下午
# @Author: ShirleyXu
# @Description: 写入数据
import time
import random
import requests

from Libs.Tool import Tool
from Libs.metricDATA import metricDATA


class ActionOpenTSDB():
    def BATCH(early_timestamp, last_timestamp, metric_name, tags ):
        ls = []
        i = early_timestamp
        while i < last_timestamp:
            for j in range(len(tags)):
                if int(i % 86400000 / 60000 + 480) == 1440:
                    data = {
                        "metric": metric_name,
                        "timestamp": i,
                        "value": metricDATA.datas(tags)[j][0],
                        "self.tags": {
                            "System": tags[j][0],
                            "Host": tags[j][1],
                            "TransactionType": tags[j][2]
                        }
                    }
                elif int(i % 86400000 / 60000 + 480) > 1440:
                    data = {
                        "metric": metric_name,
                        "timestamp": i,
                        "value": metricDATA.datas(tags)[j][int(i % 86400000 / 60000 - 960)],
                        "self.tags": {
                            "System": tags[j][0],
                            "Host": tags[j][1],
                            "TransactionType": tags[j][2]
                        }
                    }
                else:
                    data = {
                        "metric": metric_name,
                        "timestamp": i,
                        "value": metricDATA.datas(tags)[j][int(i % 86400000 / 60000 + 480)],
                        "self.tags": {
                            "System": tags[j][0],
                            "Host": tags[j][1],
                            "TransactionType": tags[j][2]
                        }
                    }
                abnormalhour = random.sample(range(24), 3)
                if int(i % 86400000 % 3600000) in abnormalhour:
                    data = {
                        "metric": metric_name,
                        "timestamp": i,
                        "value": random.randint(20, 30),
                        "self.tags": {
                            "System": tags[j][0],
                            "Host": tags[j][1],
                            "TransactionType": tags[j][2]
                        }
                    }
                ls.append(data)
                print(data)
            i += 60000
            # if len(ls) > 50:
            #     requests.Session.post(url="http://172.20.3.122:4242/api/put?details", data=ls)
            #     ls = []

    def minute(metricname, tags):
        i = 0
        while True:
            for j in range(len(tags)):
                if int(int(time.time() * 1000) % 86400000 / 60000 + 480) == 1440:
                    data = {
                        "metric": metricname,
                        "timestamp": int(time.time() * 1000),
                        # "value": random.randint(0, 10),
                        "value": metricDATA.datas(tags)[j][0],
                        "tags": {
                            "System": tags[j][0],
                            "Host": tags[j][1],
                            # "Volume": '大额'
                            "TransactionType": tags[j][2]
                        }
                    }
                elif int(int(time.time() * 1000) % 86400000 / 60000 + 480) > 1440:
                    data = {
                        "metric": metricname,
                        "timestamp": int(time.time() * 1000),
                        # "value": random.randint(0, 10),
                        "value": metricDATA.datas(tags)[j][int(i % 86400000 / 60000 - 960)],
                        "tags": {
                            "System": tags[j][0],
                            "Host": tags[j][1],
                            # "Volume": '大额'
                            "TransactionType": tags[j][2]
                        }
                    }
                else:
                    data = {
                        "metric": metricname,
                        "timestamp": int(time.time() * 1000),
                        "value": metricDATA.datas(tags)[j][int(int(time.time() * 1000) % 86400000 / 60000 + 480)],
                        "tags": {
                            "System": tags[j][0],
                            "Host": tags[j][1],
                            "TransactionType": tags[j][2]
                        }
                    }
                abnormalhour = random.sample(range(24), 3)
                if int(int(time.time() * 1000) % 86400000 % 3600000) in abnormalhour:
                    data = {
                        "metric": metricname,
                        "timestamp": int(time.time() * 1000),
                        # "value": random.randint(0, 10),
                        "value": random.randint(20, 30),
                        "tags": {
                            "System": tags[j][0],
                            "Host": tags[j][1],
                            "TransactionType": tags[j][2]
                        }
                    }
                # requests.Session.post(url="http://172.20.3.122:4242/api/put?details", data=data)
                print(data)
            time.sleep(60)

    def KAFKA_METRIC(tags, metricname, type, url):
        i = 0
        while True:
            timestamp = int(time.time() * 1000)
            for j in range(len(tags)):
                data = {
                    "type": type,
                    "url": url,
                    "labels": {
                        "System": tags[j][0],
                        "Host": tags[j][1],
                        "TransactionType": tags[j][2]
                    },
                    "name": metricname,
                    "value": random.randint(1, 600),
                    "endTime": timestamp
                }
                Tool.client_kafka().send('aiops_alert', data)
                print(data)
            # producer.close()
            i += 1
            if i % 10 == 0:
                time.sleep(120)
            else:
                time.sleep(60)

