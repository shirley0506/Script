#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @FileName: ReaderConfig.py
# @Time: 2021/7/8 6:09 下午
# @Author: ShirleyXu
# @Description: 读配置文件
import datetime
import yaml


class ReaderConfig():
    @staticmethod
    def readyaml():
        with open('/Users/shirleyxu/Code/Script/config/Insert_opentsdb.yaml', 'rb') as f:
            data = yaml.safe_load(f.read())
        return ReaderConfig.getparms(data)


    def getparms(data):
    # 分解配置文件内容
        parms = {}
        for k, v in data.items():
            if k == 'Type':
                parms[k] = v
                if data[k] == 'BATCH':
                    early_day_date = datetime.date(year=data[v]['Begin']['year'], month=data[v]['Begin']['month'], day=data[v]['Begin']['day'])
                    early_day_time = datetime.time(hour=data[v]['Begin']['hour'], minute=data[v]['Begin']['minute'], second=data[v]['Begin']['second'], microsecond=datetime.datetime.now().microsecond)
                    last_day_date = datetime.date(year=data[v]['End']['year'], month=data[v]['End']['month'], day=data[v]['End']['day'])
                    last_day_time = datetime.time(hour=data[v]['End']['hour'], minute=data[v]['End']['minute'], second=data[v]['End']['second'])
                    parms['early_timestamp'] = int(
                        datetime.datetime.combine(date=early_day_date, time=early_day_time).timestamp() * 1000)
                    parms['last_timestamp'] = int(
                        datetime.datetime.combine(date=last_day_date, time=last_day_time).timestamp() * 1000)
                elif data[k] == 'MINUTE':
                    parms[k] = v
                elif data[k] == 'CURRENT':
                    parms[k] = v
                    parms['url'] = data[v]['url']
                    parms['type'] = data[v]['type']
            elif k == 'Labels':
                parms['tags'] = data[k]
            elif k == 'MetricName':
                parms['metricname'] = data[k]
        return parms


# if __name__ == '__main__':
#     print(len(readconfig.readyaml()['tags']))
