#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @FileName: shirleyOpenTSDB.py
# @Time: 2021/7/8 6:06 下午
# @Author: ShirleyXu
# @Description: 实时、批量往OpenTSDB中写入数据
from Libs.ReaderConfig import ReaderConfig
from Libs.ActionOpenTSDB import ActionOpenTSDB



class ShirleyOpenTSDB():
    def __init__(self):
        self.parms = ReaderConfig.readyaml()


    def InsertDATA(self):
        if self.parms['Type'] == 'MINUTE':
            ActionOpenTSDB.minute(self.parms['metricname'], self.parms['tags'])
        elif self.parms['Type'] == 'BATCH':
            ActionOpenTSDB.BATCH(self.parms['early_timestamp'], self.parms['last_timestamp'], self.parms['metricname'], self.parms['tags'])
        elif self.parms['Type'] == 'CURRENT':
            ActionOpenTSDB.KAFKA_METRIC(self.parms['tags'], self.parms['metricname'],self.parms['type'], self.parms['url'])


if __name__ == '__main__':
    shirleyOpenTSDB = ShirleyOpenTSDB()
    shirleyOpenTSDB.InsertDATA()






