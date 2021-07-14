#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @FileName: shirleyOpenTSDB.py
# @Time: 2021/7/8 6:06 下午
# @Author: ShirleyXu
# @Description: 实时、批量往OpenTSDB中写入数据
from Libs.ReaderConfig import *
from Libs.ActionOpenTSDB import *


class ShirleyOpenTSDB():
    def __init__(self):
        readconfig.readyaml(self)
        self.early_timestamp = readconfig.getparms(self)[0]
        self.last_timestamp = readconfig.getparms(self)[1]
        self.function_name = readconfig.getparms(self)[2]
        self.metric_name = readconfig.getparms(self)[3]
        self.tags = readconfig.getparms(self)[4]
        self.url = readconfig.getparms(self)[5]


    def InsertDATA(self):
        if self.function_name == 'current':
            ActionOpenTSDB.CURRENT(self.metric_name, self.tags)
        elif self.function_name == 'batch':
            ActionOpenTSDB.BATCH(self.early_timestamp, self.last_timestamp, self.metric_name, self.tags)
        elif self.function_name == 'kafka':
            ActionOpenTSDB.KAFKA_METRIC(self.tags, self.metric_name, producer, type, self.url)


if __name__ == '__main__':
    shirleyOpenTSDB = ShirleyOpenTSDB()






