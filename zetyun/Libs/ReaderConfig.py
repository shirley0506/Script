#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @FileName: ReaderConfig.py
# @Time: 2021/7/8 6:09 下午
# @Author: ShirleyXu
# @Description: 读配置文件
import datetime
import yaml


class readconfig():
    def readyaml(self, path):
        with open(path, 'rb') as f:
            self.data = yaml.load(f.read(), Loader=yaml.FullLoader)

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
                self.function_name = self.data[k]
            else:
                self.metric_name = self.data[k]

        early_timestamp = int(
            datetime.datetime.combine(date=self.early_day_date, time=self.early_day_time).timestamp() * 1000)
        last_timestamp = int(datetime.datetime.combine(date=self.last_day_date, time=self.last_day_time).timestamp() * 1000)

        return early_timestamp, last_timestamp, self.function_name, self.metric_name
