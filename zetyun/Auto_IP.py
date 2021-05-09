#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @FileName: Auto_IP.py
# @Time: 2021/4/20 10:56 上午
# @Author: ShirleyXu
import random


def get_ip(number):
    # file = open('ip_list_250.txt', 'a+')
    while number > 0:
        A = random.randint(0, 255)
        B = random.randint(0, 255)
        C = random.randint(0, 255)
        D = random.randint(0, 255)
        ip = "%d.%d.%d.%d" %(A, B, C, D)
        with open('ip_list_200.txt', 'a+') as f:
            if ip in ('172.20.3.120', '172.20.3.121', '172.20.3.122', '172.20.3.170', '172.20.3.171', '172.20.3.172'):
                break
            if number == 1:
                f.writelines(ip)
            else:
                f.writelines(ip + '\n')
        number -= 1
get_ip(200)
