# -*- coding: utf-8 -*-
"""
@Title: autoFile.py
@Description:
@auther: Shirley
@Version: 1.0
@create 2018/11/14
"""
# 目标文件
filename = "E:\Program Files\JetBrains\PycharmProjects\Script\\test.txt"

#
# data = open(filename, 'r').read()
# print(data)

infile = open(filename, "w")
# datalist = ["hello", "", "world"]
for data in datalist:
    infile.writelines(data + '\n')
# infile.writelines(["hello", "", "world"])
infile.close()
infile = open(filename, "r")
print(infile.read())

