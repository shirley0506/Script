# -*- coding: utf-8 -*-
"""
@Title: findMatchlines
@Description: 打开指定目录下的所有.txt文件，并打印符合正则的行
@auther: Shirley
@Version: 1.0
@create 2019/06/20
"""


# 操作系统目录，需要os模块
import os, sys, re

datePattern = re.compile(r'\d{4}\-\d{2}\-\d{2}')
# TODO: 打开指定目录下的所有.txt文件
# des_path = sys.argv[1]
des_path = input("请输入路径：")
file_lists = os.listdir(des_path)
for file in file_lists:
    try:
        filename, extension_name = file.split('.')
    except ValueError:
        continue

    if extension_name.lower() == 'txt':
        # TODO：打印匹配正则的行
        with open(file) as f:
            lines = f.readlines()
            for line in lines:
                match_string = datePattern.match(line)
                if match_string != None:
                    print("%s文件内的：\n " % file, match_string.group())


