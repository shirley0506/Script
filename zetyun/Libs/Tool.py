#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @FileName: Tool.py
# @Time: 2021/7/16 10:49 上午
# @Author: ShirleyXu
# @Description: 各种组件
import json

from kafka import KafkaProducer


class Tool():
    @staticmethod
    def client_kafka():
        producer = KafkaProducer(
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
            # bootstrap_servers=['172.20.3.170:9092', '172.20.3.171:9092', '172.20.3.172:9092']
            bootstrap_servers=['172.20.3.120:9092', '172.20.3.121:9092', '172.20.3.122:9092']
        )
        return producer
