import datetime

a = '{"index": {"_index": "twshisplan2021", "_type": "doc", "_id": "SDF_41-__DATE__ 00:03:47"}}'
b = "{\"job_no\": \"J0149115\", \"end_time\": \"__DATE__ 00:09:17\", \"job_day\": \"__jobday__\", \"operation_no\": \"031\"," \
     "\"start_time\": \"__DATE__ 00:03:47\", \"alert_status\": 0, \"seconds\": \"384\", \"job_name\": \"SM610021\", " \
     "\"adname\": \"CBS1DAYJBATSEC\", \"job_id\": \"SDF_41\", \"interval\": 330, \"id\": \"SDF_41-__DATE__ 00:03:47\"," \
     "\"time\": \"00:06:24\", \"region\": \"CN\", \"ws\": \"CPU1\", \"run_status\": 2, \"return_code\": \"0000\", \"status\": \"C\"}"

for i in range(0, 150):
    a1 = a.replace('__DATE__', (datetime.date.today() - datetime.timedelta(days=i)).strftime("%Y-%m-%d"))
    b1 = b.replace('__DATE__', (datetime.date.today() - datetime.timedelta(days=i)).strftime("%Y-%m-%d")) \
          .replace('__jobday__', (datetime.date.today() - datetime.timedelta(days=i+1)).strftime("%Y%m%d"))
    print(a1)
    print(b1)


backup = "{ " \
            "\"_index\": \"nbuhisdata\", "\
            "\"_type\": \"doc\"," \
            "\"_id\": \"SDF_41-__DATE__ 00:07:27\", "\
            "\"_score\": 0.5138825," \
            "\"_source\": { " \
            "\"active_start\": \"2020-12-26 01:00:03\", " \
            "\"job_day\": \"__jobday__\"," \
            "\"type\": \"backup\"," \
            "\"percent\": \"1.00\"," \
            "\"job_policy\": \"APP-BOCNETGBII-LOG7-P\"," \
            "\"update_time\": \"2020-12-27 02:02:21\"," \
            "\"domain_name\": \"海鹰\"," \
            "\"active_elapsed\": 14," \
            "\"elapsed_time\": 171," \
            "\"client\": \"P2BIIOSAP04_10G\"," \
            "\"state\": \"done\"," \
            "\"id\": \"SDF_23-__DATE__ 00:07:27\"," \
            "\"run_status\": 2," \
            "\"KB_per_second\": \"825600\"," \
            "\"end_time\": \"__DATE__ 00:10:18\"," \
            "\"job_no\": \"176055\"," \
            "\"priority\": 531," \
            "\"start_time\": \"__DATE__ 00:07:27\"," \
            "\"alert_status\": 10," \
            "\"kilobytes\": 27037," \
            "\"job_id\": \"SDF_41\"," \
            "\"job_schedule\": \"diff\"," \
            "\"files\": 14," \
            "\"file_list_count\": ""," \
            "\"active_end\": \"2020-12-26 01:00:03\"," \
            "\"operation\": ""," \
            "\"status\": 0" \
            "}" \
        "}\""


'''
import datetime
import random

import numpy as np
import matplotlib.pyplot as plt
import math

u = 500  # 均值μ
# u01 = -1
sig = math.sqrt(90000)  # 标准差δ

maxvalue = 10000

x = np.linspace(0, 1439, 24 * 60)
y = (np.exp(-(x - u) ** 2 / (2 * sig ** 2)) / (math.sqrt(2 * math.pi) * sig))
mul = maxvalue / max(y)
i = 0
for num in y:
    y[i] = int(num * mul)
    i += 1
print("时间: ")
print(x)
print("值: ")
print(y[1])
print(y[720])

plt.plot(x, y, "r-", linewidth=2)
plt.grid(True)
plt.show()



import requests
import yaml

cases = [[720, 100000], [600, 200000], [900, 200000], [700, 100000],
         [540, 100000], [660, 900000], [840, 900000], [960, 900000],
         [960, 900000], [1000, 900000], [650, 900000], [660, 900000],
         [900, 200000], [840, 900000]
         ]


def send_opentsdb(json, s, url):
    result = s.post(url, json=json)


#
#
def Normaldistribution_data(u, variance):
    u = u  # 均值μ
    sig = math.sqrt(variance)  # 标准差δ
    maxvalue = 10

    x = np.linspace(0, 1439, 24 * 60)
    y = (np.exp(-(x - u) ** 2 / (2 * sig ** 2)) / (math.sqrt(2 * math.pi) * sig))
    mul = maxvalue / max(y)
    i = 0
    for num in y:
        y[i] = int(num * mul)
        i += 1

    return y


#
def datas():
    values = []
    for a in range(len(cases)):
        values.append(Normaldistribution_data(cases[a][0], cases[a][1]))
    return values


def batch(early_timestamp, last_timestamp, metric_name, tags):
    ls = []
    count = 0
    i = early_timestamp
    null_count = 1
    while i < last_timestamp:
        for j in range(len(tags)):
            if int(i % 86400000 / 60000 + 480) == 1440:
                json = {
                    "metric": metric_name,
                    "timestamp": i,
                    # "timestamp": int(time.time() * 1000),
                    # "value": random.randint(0, 10),
                    "value": datas()[j][0],
                    "tags": {
                        "System": tags[j][0],
                        "Host": tags[j][1],
                        # "Volume": '大额'
                        "TransactionType": tags[j][2]
                    }
                }
            elif int(i % 86400000 / 60000 + 480) > 1440:
                json = {
                    "metric": metric_name,
                    "timestamp": i,
                    # "timestamp": int(time.time() * 1000),
                    # "value": random.randint(0, 10),
                    "value": datas()[j][int(i % 86400000 / 60000 - 960)],
                    "tags": {
                        "System": tags[j][0],
                        "Host": tags[j][1],
                        # "Volume": '大额'
                        "TransactionType": tags[j][2]
                    }
                }
            else:
                json = {
                    "metric": metric_name,
                    "timestamp": i,
                    # "timestamp": int(time.time() * 1000),
                    # "value": random.randint(0, 10),
                    "value": datas()[j][int(i % 86400000 / 60000 + 480)],
                    "tags": {
                        "System": tags[j][0],
                        "Host": tags[j][1],
                        # "Volume": '大额'
                        "TransactionType": tags[j][2]
                    }
                }
            abnormalhour = random.sample(range(24), 3)
            if int(i % 86400000 % 3600000) in abnormalhour:
                json = {
                    "metric": metric_name,
                    "timestamp": i,
                    # "timestamp": int(time.time() * 1000),
                    # "value": random.randint(0, 10),
                    "value": random.randint(20, 30),
                    "tags": {
                        "System": tags[j][0],
                        "Host": tags[j][1],
                        # "Volume": '大额'
                        "TransactionType": tags[j][2]
                    }
                }
            # count += 1
            ls.append(json)
            # with open('./log/' + metric_name + "_指标原始数据_batch_3.txt", 'a+') as f:
            #     f.writelines(str(json) + "\n")
        i += 60000
        if len(ls) > 50:
            send_opentsdb(ls, s, url="http://172.20.3.122:4242/api/put?details")
            ls = []


if __name__ == "__main__":
    s = requests.session()

    metric_name = 'demo'
    #     # System = ['银行IC卡系统', 'ATM业务系统', 'POS业务系统']
    #     # Host = ['171.20.3.13', '172.20.3.14', '172.20.3.15', '172.20.3.16', '172.20.3.17', '172.20.3.18', '172.20.3.19',
    #     #         '172.20.3.20']
    #     # TransactionType = ['银联商户', '银联POS机', 'ATM机']
    tags = [
        ['银行IC卡系统', '171.20.3.13', '银联商户'],
        ['银行IC卡系统', '171.20.3.13', '银联POS机'],
        ['银行IC卡系统', '171.20.3.13', 'ATM机'],
        ['银行IC卡系统', '171.20.3.14', '银联商户'],
        ['银行IC卡系统', '171.20.3.14', '银联POS机'],
        ['银行IC卡系统', '171.20.3.14', 'ATM机'],
        ['银行IC卡系统', '171.20.3.15', '银联商户'],
        ['银行IC卡系统', '171.20.3.15', '银联POS机'],
        ['银行IC卡系统', '171.20.3.15', 'ATM机'],
        ['ATM业务系统', '171.20.3.16', 'ATM机'],
        ['ATM业务系统', '171.20.3.17', 'ATM机'],
        ['ATM业务系统', '171.20.3.18', 'ATM机'],
        ['POS业务系统', '171.20.3.19', '银联POS机'],
        ['POS业务系统', '171.20.3.20', '银联POS机']
    ]

    # 读配置文件，将参数以字典形式返回
    with open('./zetyun/Insert_opentsdb.yaml', 'rb') as f:
        data = yaml.load(f.read(), Loader=yaml.FullLoader)
    # 分解配置文件内容
    for k, v in data.items():
        if k == "Begin":
            early_day_date = datetime.date(year=data[k]['year'], month=data[k]['month'], day=data[k]['day'])
            early_day_time = datetime.time(hour=data[k]['hour'], minute=data[k]['minute'], second=data[k]['second'],
                                           microsecond=000)
        elif k == "End":
            last_day_date = datetime.date(year=data[k]['year'], month=data[k]['month'], day=data[k]['day'])
            last_day_time = datetime.time(hour=data[k]['hour'], minute=data[k]['minute'], second=data[k]['second'])
        elif k == "Action":
            function_name = data[k]
    # 整合开始/结束时间戳
    early_timestamp = int(datetime.datetime.combine(date=early_day_date, time=early_day_time).timestamp() * 1000)
    last_timestamp = int(datetime.datetime.combine(date=last_day_date, time=last_day_time).timestamp() * 1000)
    # 通过参数，执行对应方法
    if function_name == 'batch':
        batch(early_timestamp, last_timestamp, metric_name, tags)
'''
