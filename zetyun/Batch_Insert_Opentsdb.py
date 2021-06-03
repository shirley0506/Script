#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
# 修改要求：
# 1. 能加上清理的动作: 清理指标数据、阈值，清理MySQL表
'''
import datetime
import time
import random

import pymysql
import requests
from datetime import datetime as dt
from kafka import KafkaProducer
import json
import yaml


def send_opentsdb(json, s, url):
    result = s.post(url, json=json)
    # print(result.text)


def create_kafka_producer_session():
    producer = KafkaProducer(
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        # bootstrap_servers=['172.20.3.170:9092', '172.20.3.171:9092', '172.20.3.172:9092']
        bootstrap_servers=['172.20.3.120:9092', '172.20.3.121:9092', '172.20.3.122:9092']
    )
    return producer


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


# 指标数据：实时写入
def current(metric_name, tags, s):
    ls = []
    i = 0
    while True:
        for i in range(len(tags)):
            json = {
                "metric": metric_name,
                "timestamp": int(time.time() * 1000),
                "value": random.uniform(1, 600),
                # "value": 100,
                "tags": {
                    "host": tags[i][0],
                    "path": tags[i][1],
                    "port": tags[i][2]
                }
            }
            ls.append(json)
            # with open('metric.txt', 'a') as f:
            #     f.write(str(json) + '\n')
        send_opentsdb(ls, s, url="http://172.20.3.122:4242/api/put?details")
        i += 1
        if i % 30 == 0:
            with open('./log/' + str(metric_name) + '_空值时间_current.txt', 'a') as f:
                f.writelines("空值的时间为: " + datetime.datetime.fromtimestamp(float(time.time())).strftime("%Y-%m-%d %H:%M:%S.%f")[
                                 :-3] + "\n")
            time.sleep(180)
        else:
            time.sleep(30)
        ls = []


# 批量发数据
# 直接传时间戳，并间隔发空值
def batch(early_timestamp, last_timestamp, metric_name, tags):
    ls = []
    count = 0
    i = early_timestamp
    null_count = 1
    while i < last_timestamp:
        for j in range(len(tags)):
            json = {
                "metric": metric_name,
                "timestamp": i,
                # "timestamp": int(time.time() * 1000),
                "value": random.uniform(1, 600),
                "tags": {
                    "host": tags[j][0],
                    "path": tags[j][1],
                    "port": tags[j][2]
                }
            }
            with open('./log/' + metric_name + "_指标原始数据_batch.txt", 'a+') as f:
                f.writelines(str(json) + "\n")
            ls.append(json)
        count += 1
        if len(ls) > 50:
            send_opentsdb(ls, s, url="http://172.20.3.122:4242/api/put?details")
            ls = []
        if count % 60 == 0:
            with open('./log/' + metric_name + "_空值记录_batch.log", 'a+') as f:
                a = i
                for a in range(a, a + 180000, 30000):
                    '''
                    fromtimestamp：13位时间戳转化为本地时区时间
                    utcfromtimestamp: 13位时间戳转化为0时区时间
                    '''
                    f.writelines("第" + str(null_count) + "个空值时间：" +
                                 datetime.datetime.fromtimestamp(float(a) / 1000).strftime("%Y-%m-%d %H:%M:%S.%f")[
                                 :-3] + '\n')
                    null_count += 1
            i += 180000
        else:
            i += 30000


# 发送Kafka metric数据
def send_metric_kafka(tags, metric_name, topic, producer, type, url):
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


# 清理数据库的相关数据
def clean_mysql_data(metric_name):
    # 定义数据库信息
    connect = pymysql.Connect(
        host='172.20.3.120',
        port=3306,
        user='root',
        passwd='MySQL!23',
        db='aiops',
        charset='utf8'
    )
    # 创建数据库连接并返回游标
    cursor = connect.cursor()
    # sql语句
    sql1 = "delete from alert_calculation_data where metricTagsId in " \
           "(select id from metric_tags where metric_tags.metric like '%" + metric_name + "%')"
    sql2 = "delete from metric_tags where metric like '%" + metric_name + "%')"
    # 执行SQL语句
    cursor.execute(sql1)
    time.sleep(5)
    cursor.execute(sql2)
    cursor.close()
    connect.close()


def clean_opentsdb_data(start, end, metric_name):
    requests.delete()


def metric_tags(count):
    metric_tags = []
    for i in count:
        metric_tags.append([])
        metric_tags[i].append('172.20.3.120')
        metric_tags[i].append(i)


if __name__ == "__main__":
    s = requests.session()
    # variable_parameter = []
    metric_name = 'xuqq_abnormalDay_3'
    tags = [
        ['172.20.3.120', '/opt/mml/log/mmlapi/info_1.log', 13100],
        ['172.20.3.121', '/opt/mml/log/mmlapi/info_2.log', 13101],
        ['172.20.3.122', '/opt/mml/log/mmlapi/info_3.log', 13102]
    ]
    metric_topic = 'aiops_metric'
    producer = create_kafka_producer_session()
    type = 'prometheus'
    url = 'http://172.20.3.120:9090'
    # 读配置文件，将参数以字典形式返回
    with open('Insert_opentsdb.yaml', 'rb') as f:
        data = yaml.load(f.read(), Loader=yaml.FullLoader)
    # 分解配置文件内容
    for k, v in data.items():
        if k == "Begin":
            early_day_date = datetime.date(year=data[k]['year'], month=data[k]['month'], day=data[k]['day'])
            early_day_time = datetime.time(hour=data[k]['hour'], minute=data[k]['minute'], second=data[k]['second'],
                                           microsecond=datetime.datetime.now().microsecond)
        elif k == "End":
            last_day_date = datetime.date(year=data[k]['year'], month=data[k]['month'], day=data[k]['day'])
            last_day_time = datetime.time(hour=data[k]['hour'], minute=data[k]['minute'], second=data[k]['second'])
        elif k == "Action":
            function_name = data[k]
    # 整合开始/结束时间戳
    early_timestamp = int(datetime.datetime.combine(date=early_day_date, time=early_day_time).timestamp() * 1000)
    last_timestamp = int(datetime.datetime.combine(date=last_day_date, time=last_day_time).timestamp() * 1000)
    # 通过参数，执行对应方法
    if function_name == 'current':
        current(metric_name, tags, s)
    elif function_name == 'batch':
        batch(early_timestamp, last_timestamp, metric_name, tags)
    elif function_name == 'kafka':
        send_metric_kafka(tags, metric_name, metric_topic, producer, type, url)

