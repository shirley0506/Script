# -*- coding:UTF-8 -*-
"""
@Title: remoteFiles
@author: Shirley
@create: 2019-06-12
@Description: 对远程服务器写文件
"""

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname='172.20.3.122', port=22, username='root', password='123456')

stdin, stdout, stderr = ssh.exec_command('cd /home/test; ls -l')

result = stdout.read()

print(result)

ssh.close()

