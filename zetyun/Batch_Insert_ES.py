import datetime
from datetime import timezone
import time
from random import randint

from elasticsearch import helpers
from elasticsearch import Elasticsearch
import time


def WriteES():
    es = Elasticsearch(hosts=['172.20.3.120:9200'])

    base = datetime.datetime.today()
    # numdays = 100
    num2 = 1000000
    num1 = 100
    # docunum = 100
    i = 0
    j = 0
    actions = []
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
    while (i < num1):
        while (j < num2 ):
            # d1 = base - datetime.timedelta(days=j)
            now = datetime.datetime.now()
            usetime = (now - datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            # ts = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            action = {
                "_index": "testbatch05_2020.01.15",
                "_type": "doc",
                "_source": {
                    "@timestamp": usetime,
                    "message": "2020-01-13 00:00:19.217 [http-nio-13111-exec-6] INFO  com.zetyun.aiops.mmlapi.aop.LogAspect"
                               " - [RESPONSE]URL:http://API-SERVER/metricalert/alert/batchAlertWithDbList, DURATION:24 ms",
                    "@thread_lineno": 2,
                    "@source_type": "mmlapi_new_copy",
                    "@source": "/opt/mml/log/mmlapi/info.log",
                    "@lineno": 6,
                    "@threadname": "http-nio-13111-exec-6",
                    "@index_date": "2020.01.13"
                }
            }
            actions.append(action)
            j += 1
            helpers.bulk(es, actions)
        # time.sleep(1)
        i += 1


if __name__ == '__main__':
    WriteES()
    print('work done!')
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])