#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @FileName: shirleyOpenTSDB.py
# @Time: 2021/7/8 6:06 下午
# @Author: ShirleyXu
# @Description: 实时、批量往OpenTSDB中写入数据
from Libs.ReaderConfig import *
from Libs.ActionOpenTSDB import *

class shirleyOpenTSDB():
    def __init__(self, path):
        readconfig.readyaml(self, path)
        self.parms = readconfig.getparms(self)


    def insertDATA(self):
        if self.function_name == 'current':
            ActionOpenTSDB.CURRENT(metric_name, tags, s)
        elif self.function_name == 'batch':
            ActionOpenTSDB.BATCH(early_timestamp, last_timestamp, metric_name, tags)
        elif self.function_name == 'kafka':
            ActionOpenTSDB.KAFKA_METRIC(tags, metric_name, metric_topic, producer, type, url)


if __name__ == '__main__':
    shirleyOpenTSDB = shirleyOpenTSDB('/Users/shirleyxu/Code/Script/config/Insert_opentsdb.yaml')





