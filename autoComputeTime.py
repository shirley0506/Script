# -*- coding:UTF-8 -*-
"""
@Title: autoComputeTime
@Author: Shirley
@Creat: 2019-06-12
@Version: 1.0
@Description：为了自动计算LogCollector采集花费的时间
"""
import datetime


def compute_collector_time(log, msg, events):
    # 创建一个列表，存储包含events的索引，方便把处于发送阶段的日志截取出来
    events_index = []
    for message in msg:
        if 'events' in message:
            message_index = msg.index(message)
            events_index.append(message_index)
            # print(msg.index(message))
            # events_index.append(msg.index(message))

    # 创建新列表，存储处于发送阶段的日志
    events_messages = []
    for index in events_index:
        events_log = msg[index]
        events_messages.append(events_log.strip())
        # events_message.append(msg[index])

    # 计算日志中显示的采集个数
    succeed_messages = []
    succeed_split = []
    for event in events_messages:
        if 'Succeed' in event:
            succeed_messages.append(event)

    for s in succeed_messages:
        succeed_split.append(s.split(' '))

    count1 = 0
    for i in succeed_split:
        batch_events = int(i[-2])
        count1 += batch_events

    if count1 == events:
        print("{} 采集数量正确：".format(log, count1))
    else:
        print('{} 采集数量错误，原始文件行数：{},实际采集数量：{}'.format(log, events, count1))

    # 获取开始/结束采集的两条日志
    first_log = events_messages[0]
    last_log = events_messages[-1]

    # 获取开始/结束采集的日期，和时间
    starting = first_log.split(' ')
    end = last_log.split(' ')
    starting_time = starting[0] + ' ' + starting[1] + '000'
    end_time = end[0] + ' ' + end[1] + '000'
    print("{} 开始时间：{}".format(log, starting_time))
    print("{} 结束时间：{}".format(log, end_time))

    # 转化时间格式
    a = datetime.datetime.strptime(starting_time, '%Y-%m-%d %H:%M:%S,%f')
    b = datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S,%f')

    print("{} 相差时间：{}".format(log, b-a))
    return b-a


# 定义一个空列表，存储用户输入的文件路径
logs = input("请输入文件的全路径，若有多个路径，请用英文逗号隔开:")
log_path = logs.split(',')
events = int(input("请输入原始文件行数："))

for log in log_path:
    file = open(log, 'r')
    # 读取所有行，返回列表
    msg = [line for line in file.readlines()]
    compute_collector_time(log, msg, events)

"""
最大的错误，readline是读取整行的字符
# 把文件内容读取出来，并存储到列表msg中
while True:
    msg.append(file.readline())
    # print(msg)
    if not :
        break
    count += 1
print(count)
"""








