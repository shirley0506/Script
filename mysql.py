#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @FileName: SSH_linux.py
# @Time: 2021/5/23 12:08 下午
# @Author: ShirleyXu
# @Description: 操作MySQL数据库


import pymysql.cursors

connect = pymysql.Connect(
    host='172.20.3.120',
    port=3306,
    user='root',
    passwd='MySQL!23',
    db='aiops',
    charset='utf8'
)

cursor = connect.cursor()

sql = 'delete from alert_calculation_data where metricTagsId in ' \
      '(select id from metric_tags where metric_tags.metric like "%" + metric_name + "%")'

# sql = 'select * from alert_calculation_data'
# sql = 'select * from metric_tags'



cursor.execute(sql)
for row in cursor.fetchall():
    print(row)

cursor.close()
connect.close()

table1 = 'alert_calculation_data'
table2 = 'metric_tags'
column1 = 'metricTagsId'
column2 = 'id'
column3 = 'metric'

