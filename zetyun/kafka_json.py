# 修改要求：
# 1. 参数化


import random

from kafka import KafkaProducer
import json
from datetime import datetime
import time

# 发送JSON格式的数据

producer = KafkaProducer(
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    # bootstrap_servers=['172.20.3.170:9092', '172.20.3.171:9092', '172.20.3.172:9092']
    bootstrap_servers=['172.20.3.120:9092', '172.20.3.121:9092', '172.20.3.122:9092']
)

'''
# 发送普通JSON至topic
data = {
        "__fields": [],
        "__hostname": "92.162.96.66.static.eigbox.net",
        "__ip": "172.20.3.120",
        "__messages": [
            "2020-05-15 16:33:12.496 [http-nio-13111-exec-1] INFO  "
            "com.zetyun.aiops.mmlapi.aop.ApiRequestHandlerInterceptor - X-Service-Caller？alertSink "
        ],
        "__offset": 20083,
        "__seq": 4272299,
        "__source": "/opt/mml/log/mmlapi/info.log",
        "__thread": [
            ""
        ]
    }

topics = []

for i in range(1, 208):
    a = 'test_xu_' + str(i)
    topics.append(a)

while True:

    for topic in topics:
        producer.send(topic, data)
    time.sleep(0.1)    

producer.close()    
'''


# aiops_metric的指标数据


# 指标处理的topic


def send_metric_kafka(IP, name, topic):
    while True:
        timestamp = int(time.time() * 1000)
        for ip in IP:
            data = {
                "type": "opentsdb",
                "url": "http://172.20.3.122:4242",
                "labels": {
                    "host": ip
                },
                "name": name,
                "value": random.randint(1, 12),
                "endTime": timestamp

            }
            producer.send(topic, data)
        producer.close()
        time.sleep(60)


if __name__ == "__main__":
    topic = 'aiops_metric'
    name = 'xuqq_abnomalDay_1'
    IP = ['172.20.3.120', '172.20.3.121', '172.20.3.122']
