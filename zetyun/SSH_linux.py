#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @FileName: SSH_linux.py
# @Time: 2021/5/8 11:34 上午
# @Author: ShirleyXu
# @Description: scp上传本地文件到Linux服务器

import paramiko
from scp import SCPClient


def connect_host(host, port, user, passwd):
    # ssh登录远程服务器
    Client = paramiko.SSHClient()
    Client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    Client.connect(hostname=host, port=port, username=user, password=passwd)
    return Client


def main(client, local_file, remote_path):
    # 主函数，传文件
    scp = SCPClient(client.get_transport())
    try:
        scp.put(local_file, remote_path)
    except FileNotFoundError as e:
        print(e)
        print("文件不存在" + local_file)
    else:
        print("文件上传成功")
        client.close()


if __name__ == '__main__':
    local_file = '/Users/shirleyxu/Pycharm/Script/logs/example.txt'
    remote_path = '/mnt/disk01'
    Host = '172.20.3.120'
    User = 'root'
    Passwd = 'asdqwe123'
    Port = 22
    client = connect_host(Host, Port, User, Passwd)
    main(client, local_file, remote_path)
