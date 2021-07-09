#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @FileName: ActionOpenTSDB.py
# @Time: 2021/7/9 4:58 下午
# @Author: ShirleyXu
# @Description: 写入数据
from datetime import time
from random import random

import requests

from MetricDATA import *


class ActionOpenTSDB():
    def __init__(self, early_timestamp, metric_name, last_timestamp, tags, ):
        self.early_timestamp = early_timestamp
        self.last_timestamp = last_timestamp
        self.self.metric_name = metric_name
        self.self.tags = tags

    def BATCH(self):
        ls = []
        i = self.early_timestamp
        while i < self.last_timestamp:
            for j in range(len(self.self.tags)):
                if int(i % 86400000 / 60000 + 480) == 1440:
                    json = {
                        "metric": self.metric_name,
                        "timestamp": i,
                        "value": MetricDATAS.datas()[j][0],
                        "self.tags": {
                            "System": self.tags[j][0],
                            "Host": self.tags[j][1],
                            "TransactionType": self.tags[j][2]
                        }
                    }
                elif int(i % 86400000 / 60000 + 480) > 1440:
                    json = {
                        "metric": self.metric_name,
                        "timestamp": i,
                        "value": MetricDATAS.datas()[j][int(i % 86400000 / 60000 - 960)],
                        "self.tags": {
                            "System": self.tags[j][0],
                            "Host": self.tags[j][1],
                            "TransactionType": self.tags[j][2]
                        }
                    }
                else:
                    json = {
                        "metric": self.metric_name,
                        "timestamp": i,
                        "value": MetricDATAS.datas()[j][int(i % 86400000 / 60000 + 480)],
                        "self.tags": {
                            "System": self.tags[j][0],
                            "Host": self.tags[j][1],
                            "TransactionType": self.tags[j][2]
                        }
                    }
                abnormalhour = random.sample(range(24), 3)
                if int(i % 86400000 % 3600000) in abnormalhour:
                    json = {
                        "metric": self.metric_name,
                        "timestamp": i,
                        "value": random.randint(20, 30),
                        "self.tags": {
                            "System": self.tags[j][0],
                            "Host": self.tags[j][1],
                            "TransactionType": self.tags[j][2]
                        }
                    }
                ls.append(json)
            i += 60000
            if len(ls) > 50:
                requests.Session.post(url="http://172.20.3.122:4242/api/put?details", json=ls)
                ls = []

    def CURRENT(self):
        i = 0
        while True:
            for j in range(len(self.tags)):
                if int(int(time.time() * 1000) % 86400000 / 60000 + 480) == 1440:
                    json = {
                        "metric": self.metric_name,
                        "timestamp": int(time.time() * 1000),
                        # "value": random.randint(0, 10),
                        "value": MetricDATAS.datas()[j][0],
                        "tags": {
                            "System": self.tags[j][0],
                            "Host": self.tags[j][1],
                            # "Volume": '大额'
                            "TransactionType": self.tags[j][2]
                        }
                    }
                elif int(int(time.time() * 1000) % 86400000 / 60000 + 480) > 1440:
                    json = {
                        "metric": self.metric_name,
                        "timestamp": int(time.time() * 1000),
                        # "value": random.randint(0, 10),
                        "value": MetricDATAS.datas()[j][int(i % 86400000 / 60000 - 960)],
                        "tags": {
                            "System": self.tags[j][0],
                            "Host": self.tags[j][1],
                            # "Volume": '大额'
                            "TransactionType": self.tags[j][2]
                        }
                    }
                else:
                    json = {
                        "metric": self.metric_name,
                        "timestamp": int(time.time() * 1000),
                        "value": MetricDATAS.datas()[j][int(int(time.time() * 1000) % 86400000 / 60000 + 480)],
                        "tags": {
                            "System": self.tags[j][0],
                            "Host": self.tags[j][1],
                            "TransactionType": self.tags[j][2]
                        }
                    }
                abnormalhour = random.sample(range(24), 3)
                if int(int(time.time() * 1000) % 86400000 % 3600000) in abnormalhour:
                    json = {
                        "metric": self.metric_name,
                        "timestamp": int(time.time() * 1000),
                        # "value": random.randint(0, 10),
                        "value": random.randint(20, 30),
                        "tags": {
                            "System": self.tags[j][0],
                            "Host": self.tags[j][1],
                            "TransactionType": self.tags[j][2]
                        }
                    }
                requests.Session.post(url="http://172.20.3.122:4242/api/put?details", json=json)
            time.sleep(60)

    def KAFKA_METRIC(self):
        i = 0
        while True:
            timestamp = int(time.time() * 1000)
            for j in range(len(tags)):
                data = {
                    "type": type,
                    "url": url,
                    "labels": {
                        "host": tags[j][0],
                        "path": tags[j][1],
                        "port": tags[j][2]
                    },
                    "name": metric_name,
                    "value": random.randint(1, 600),
                    "endTime": timestamp
                }
                producer.send(topic, data)
                with open('./log/' + str(metric_name) + '_原始记录_kafka.log', 'a+') as f:
                    f.writelines(str(data) + '\n')
                # print(data)
            # producer.close()
            i += 1
            if i % 10 == 0:
                time.sleep(120)
            else:
                time.sleep(60)

