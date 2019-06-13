# -*- coding: utf-8 -*-
"""
@Title: circleFiles
@Description: 循环写文件
@auther: Shirley
@Version: 1.0
@create 2019/06/11
"""

import os
import datetime

filename = input("请输入文件名：")

# 开始时间
startTime = datetime.datetime.now()
# 1H后结束
# endTime = startTime + datetime.timedelta(hours=1)
endTime = startTime + datetime.timedelta(seconds=10)
# print(endTime)
# a = str(endTime - datetime.datetime.now())
# if a < '0:00:00.000000':
#     print(True)
# else:
#     print(False)

while str(endTime - datetime.datetime.now()) > '0:00:00.000000':
    path = os.getcwd()
    fo = open(path + '/' + filename, 'a+')
    log_time = str(datetime.datetime.now())[:-3]
    message = 'http-nio-13111-exec-3] INFO  com.zetyun.aiops.mmlapi.aop.LogAspect - ' \
              '[REQUEST]URL:http://172.20.3.120:13111/template/simpleParse, METHOD:POST, PARAMETER:' \
              '[{"log":"2017-01-01 23:15:00\tLocal7.Error\t10.194.254.241\tJan  1 23:14:14 2017 S7506E-B ' \
              '%%10OSPF/3/IF_CFG_ERROR(t): OSPF TrapID1.3.6.1.2.1.14.16.2.4<ospfIfConfigError>: ' \
              'Non-virtual interface 10.194.204.242 index 0 Router 192.168.250.253 PacketSrc 20.194.82.254 ' \
              'config error 2 PacketType 1.","patterns":["(?<logtime>\\d+)"]}], ' \
              'USERID:0f543e60-e55d-4a76-aa10-6e56e8b8e167, USERNAME:admin'
    msg = log_time + ' ' + message
    fo.write(msg + '\n')
    fo.close()
