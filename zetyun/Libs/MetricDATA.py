#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @FileName: MetricDATAS.py
# @Time: 2021/7/9 5:07 下午
# @Author: ShirleyXu
# @Description: 指标数据生成
import math

import numpy as np


class MetricDATAS():
    def __init__(self, u, variance, cases):
        self.u = u
        self.variance = variance
        self.cases = cases

    def Normaldistribution_data(self, u, variance):
        u = u  # 均值μ
        sig = math.sqrt(variance)  # 标准差δ
        maxvalue = 10000
        x = np.linspace(0, 1439, 24 * 60)
        y = (np.exp(-(x - u) ** 2 / (2 * sig ** 2)) / (math.sqrt(2 * math.pi) * sig))
        mul = maxvalue / max(y)
        i = 0
        for num in y:
            y[i] = int(num * mul)
            i += 1
        return y

    def datas(self):
        values = []
        for a in range(len(self.cases)):
            values.append(self.Normaldistribution_data(self.cases[a][0], self.cases[a][1]))
        return values


