#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @FileName: ReaderConfig.py
# @Time: 2021/7/8 6:09 下午
# @Author: ShirleyXu
# @Description: 读配置文件
import datetime
import yaml


class readconfig():
    def readyaml(self):
        with open('/Users/shirleyxu/Code/Script/config/Insert_opentsdb.yaml', 'rb') as f:
            self.data = yaml.safe_load(f.read())

    def getparms(self):
    # 分解配置文件内容
        for k, v in self.data.items():
            if k == "Begin":
                self.early_day_date = datetime.date(year=self.data[k]['year'], month=self.data[k]['month'], day=self.data[k]['day'])
                self.early_day_time = datetime.time(hour=self.data[k]['hour'], minute=self.data[k]['minute'], second=self.data[k]['second'], microsecond=datetime.datetime.now().microsecond)
            elif k == "End":
                self.last_day_date = datetime.date(year=self.data[k]['year'], month=self.data[k]['month'], day=self.data[k]['day'])
                self.last_day_time = datetime.time(hour=self.data[k]['hour'], minute=self.data[k]['minute'], second=self.data[k]['second'])
            elif k == "Action":
                function_name = self.data[k]
            elif k == "MetricName":
                metric_name = self.data[k]
            elif k == "Labels":
                tags = self.data[k]
            elif k == "URL":
                url = self.data[k]

        early_timestamp = int(
            datetime.datetime.combine(date=self.early_day_date, time=self.early_day_time).timestamp() * 1000)
        last_timestamp = int(datetime.datetime.combine(date=self.last_day_date, time=self.last_day_time).timestamp() * 1000)

        return early_timestamp, last_timestamp, function_name, metric_name, tags, url
