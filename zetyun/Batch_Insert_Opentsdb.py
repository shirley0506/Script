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
def current(metric_name, IP, s):
    ls = []
    i = 0
    while True:
        for ip in IP:
            json = {
                "metric": metric_name,
                "timestamp": int(time.time() * 1000),
                "value": random.randint(1, 600),
                # "value": 100,
                "tags": {
                    "host": ip
                }
            }
            ls.append(json)
            # with open('metric.txt', 'a') as f:
            #     f.write(str(json) + '\n')
        send_opentsdb(ls, s, url="http://172.20.3.122:4242/api/put?details")
        i += 1
        if i % 30 == 0:
            with open('metric.txt', 'a') as f:
                f.writelines("空值的时间戳为" + str(int(time.time() * 1000)) + "\n")
            time.sleep(180)
        else:
            time.sleep(60)
        ls = []


# 批量写入指标数据
# def batch(a, metric_name, s, value_min, value_max, hour):
#     # s = requests.Session()
#     ls = []
#     for i in range(1, hour * 60):
#         for ip in IP:
#             # 多序列指标
#             json = {
#                 "metric": metric_name,
#                 "timestamp": a,
#                 # "timestamp": int(time.time() * 1000),
#                 "value": random.randint(value_min, value_max),
#                 "tags": {
#                     "host": ip
#                 }
#             }
#             # with open('metric.txt', 'a') as f:
#             #     f.writelines(str(json) + '\n')
#             ls.append(json)
#         if len(ls) > 50:
#             send_opentsdb(ls, s, url="http://172.20.3.122:4242/api/put?details")
#             ls = []
#         if i % 60 == 0:
#             a -= 180000
#             i += 1
#             with open('metric.txt', 'a') as f:
#                 f.writelines("空值的时间戳为" + str(a + 60000) + "\n")
#         else:
#             a -= 60000
#             i += 1


# 批量发数据
# 直接传时间戳，并间隔发空值
def batch(early_timestamp, last_timestamp, metric_name):
    ls = []
    count = 0
    i = last_timestamp
    while i > early_timestamp:
        for ip in IP:
            json = {
                "metric": metric_name,
                "timestamp": i,
                # "timestamp": int(time.time() * 1000),
                "value": random.randint(1, 600),
                "tags": {
                    "host": ip
                }
            }
            ls.append(json)
        count += 1
        if len(ls) > 50:
            send_opentsdb(ls, s, url="http://172.20.3.122:4242/api/put?details")
            ls = []
        if count % 10 == 0:
            with open(metric_name + "_metric.log", 'a+') as f:
                f.writelines(metric_name + "空值的时间戳为" + str(i - 60000) + "\n")
            i -= 180000
        else:
            i -= 60000


# 发送Kafka metric数据
def send_metric_kafka(IP, name, topic, producer, type, url):
    i = 0
    while True:
        timestamp = int(time.time() * 1000)
        for ip in IP:
            data = {
                "type": type,
                "url": url,
                "labels": {
                    "host": ip
                },
                "name": name,
                "value": random.randint(1, 600),
                "endTime": timestamp

            }
            producer.send(topic, data)
            with open(str(name) + 'metric_kafka.log', 'a+') as f:
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
    variable_parameter = []
    metric_name = 'xuqq_abnormalDay_4'
    IP = ['172.20.3.120', '172.20.3.121', '172.20.3.122']
    metric_topic = 'aiops_metric'
    producer = create_kafka_producer_session()
    # 批量写指标数据
    # last_day = 25
    # early_day = 25
    # b = random.randint(1, 100)
    # hour = 11
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
    #     variable = {'month': 5, 'day': day, 'hour': hour, 'minute': 0}
    #     past_timestamp = assign_timestamp(**variable)
    #     batch(past_timestamp, metric_name, s, value_min, value_max, hour)
    # 实时写入opentsdb
    # current(metric_name, IP, s)
    # 发送Kafka metric数据
    type = 'prometheus'
    url = 'http://172.20.3.120:9090'
    send_metric_kafka(IP, metric_name, metric_topic, producer, type, url)
    # 按照时间戳，批量发数据
    # last_day_date = datetime.date(year=2021, month=5, day=27)
    # early_day_date = datetime.date(year=2021, month=5, day=27)
    # last_day_time = datetime.time(hour=15, minute=00, second=0)
    # early_day_time = datetime.time(hour=14, minute=30, second=0)
    # last_timestamp = int(datetime.datetime.combine(date=last_day_date, time=last_day_time).timestamp() * 1000)
    # early_timestamp = int(datetime.datetime.combine(date=early_day_date, time=early_day_time).timestamp() * 1000)
    # batch(early_timestamp, last_timestamp, metric_name)