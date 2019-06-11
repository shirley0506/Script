# -*- coding: utf-8 -*-
"""
@Title: autoFiles.py
@Description: 生成指定行数、指定文件个数
@auther: Shirley
@Version: 2.0
@create 2019/06/11
"""

import datetime

def create_files(filename, msg):
    parent_path = "/Users/shirleyxu/Documents/Script/Python"
   # filename = 'test01'
    full_path = parent_path + '/' + filename + '.txt'
    f_create = open(full_path, 'a+')
    f_create.write(msg + '\n')
    f_create.close()


message = 'http-nio-13111-exec-3] INFO  com.zetyun.aiops.mmlapi.aop.LogAspect - ' \
          '[REQUEST]URL:http://172.20.3.120:13111/template/simpleParse, METHOD:POST, PARAMETER:' \
          '[{"log":"2017-01-01 23:15:00\tLocal7.Error\t10.194.254.241\tJan  1 23:14:14 2017 S7506E-B ' \
          '%%10OSPF/3/IF_CFG_ERROR(t): OSPF TrapID1.3.6.1.2.1.14.16.2.4<ospfIfConfigError>: ' \
          'Non-virtual interface 10.194.204.242 index 0 Router 192.168.250.253 PacketSrc 20.194.82.254 ' \
          'config error 2 PacketType 1.","patterns":["(?<logtime>\\d+)"]}], ' \
          'USERID:0f543e60-e55d-4a76-aa10-6e56e8b8e167, USERNAME:admin'


lineno = int(input("行数："))
i = 0
now = str(datetime.datetime.now())[:-3]
msg = now + '  ' + message
while i < lineno:
    create_files('test01', msg)
    i += 1

