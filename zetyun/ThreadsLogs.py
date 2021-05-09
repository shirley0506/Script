#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @FileName: AutoLogs.py
# @Time: 2021/4/16 10:27 上午
# @Author: ShirleyXu
# Description: 实现多线程并发写日志，每条日志都有编号


# Python的多线程是并发原理
# 同步原语
# _thread  隐晦的约定：主线程一旦停了，子线程都会停

import random
from datetime import datetime
import threading
import time
import logging

logging.basicConfig(level=logging.INFO)
loops = [2, 4]
path = '/Users/shirleyxu/Pycharm/Script/logs/'
loglevel = ['ERROR', 'WARN', 'INFO', 'Debug']
sample = "__TIME__  [error] : rewrite or internal redirection cycle while internally redirecting " \
         "to \"/index.html\", client: 192.168.0.228, server: , request: \"GET /favicon.ico HTTP/1.1\", " \
         "host: \"172.20.3.120:3100\", referrer: \"http://172.20.3.120:3100/log/elasticsearchmanager\" __ID__\n "


def write_messages(log_id):
    global id
    id = 0
    while id < log_id:
        with open(path + 'example.txt', 'a+') as f:
            id += 1
            message_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            log = sample.replace('__TIME__', message_time) \
                .replace('[error]', "[" + random.choice(loglevel) + "]") \
                .replace('__ID__', str(id))
            f.writelines(log)
    print(log_id)


def main():
    logging.info("main start at " + time.ctime())
    locks = []
    threads = []
    nloops = range(2)

    for i in nloops:
        t = threading.Thread(target=write_messages, args=(10000,))
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    logging.info("main end at " + time.ctime())


if __name__ == "__main__":
    main()
