# -*- coding:UTF-8 -*-
"""
@Title: averageTime
@Author: Shirley
@Creat/Update: 2019-06-13
@Version: 2.0
@Description：在原autoComputeTime的基础上封装函数，同时计算平均耗时
"""
import datetime


# 获取日志全文，并返回
def read_log(filename):
    fo = open(filename, 'r')
    msg = [line.strip() for line in fo.readlines()]
    return msg


# 获取含有events的日志，并返回
def getEventsMessage(messages):
    # 创建一个列表，存储包含events的索引，方便把处于发送阶段的日志截取出来
    events_message = []
    for message in messages:
        if 'events' in message:
            # message_index = msg.index(message)
            events_message.append(message)
    return events_message


# 获取日志总发送的events之和，并打印发送的数据量是否有出入
def succeededEvents(eventslog, exceptevents, filename):
    succeed_messages = []
    succeed_split = []
    for event in eventslog:
        if 'Succeed' in event:
            succeed_messages.append(event)

    for s in succeed_messages:
        succeed_split.append(s.split(' '))

    count = 0
    for i in succeed_split:
        batch_events = int(i[-2])
        count += batch_events

    if count == exceptevents:
        print("{} 采集数量正确：".format(filename, count))
    else:
        print('{} 采集数量错误，原始文件行数：{},实际采集数量：{}'.format(filename, exceptevents, count))


# 取每个文件的时间差，并返回时间差
def getdiffTime(filename, events_message):
    # 获取开始/结束采集的两条日志
    first_log = events_message[0]
    last_log = events_message[-1]
    # 获取开始/结束采集的日期，和时间
    starting = first_log.split(' ')
    end = last_log.split(' ')
    starting_time = starting[0] + ' ' + starting[1] + '000'
    end_time = end[0] + ' ' + end[1] + '000'
    print("{} 开始时间：{}".format(filename, starting_time))
    print("{} 结束时间：{}".format(filename, end_time))
    # 转化时间格式
    a = datetime.datetime.strptime(starting_time, '%Y-%m-%d %H:%M:%S,%f')
    b = datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S,%f')

    print("{} 相差时间：{}".format(filename, (b - a)[:-3]))
    return (b - a)[:-3]


# 计算平均值
def getaverageTime(batchTimes):
    num = 0
    sumTime = 0
    for batchTime in batchTimes:
        sumTime += batchTime
        num += 1
    print("平均时间：", sumTime / num)


if __name__ == '__main__':
    # 由终端获取文件列表，预期日志数量
    logslist = input("请输入文件的全路径，若有多个路径，请用英文逗号隔开:")
    log_path = logslist.split(',')
    # events = int(input("请输入原始文件行数："))
    # 读取日志内容
    mylog = []
    for filename in log_path:
        mylog.append(read_log(filename))

    # 处理每个日志文件内包含events的信息
    for i in range(0, len(mylog)):
        getEventsMessage(i)














