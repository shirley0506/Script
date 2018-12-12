# -*- coding: utf-8 -*-
"""
@Title: exercise.py
@Description:
@auther: Shirley
@Version: 1.0
@create 2018/11/21
"""
"""
# 练习format方法
name = "Shirley"
age = 28
working_age = 5
lanuage = "Python"
method = "foramt"

print("{0} now is {1} and have worked {2} years" .format(name, age, working_age))
print("{0} is now learning lanuage--{1} and lear how to use method-{2}" .format(name, lanuage, method))
"""

"""
# python3的新功能 字符串f可以格式化输出
name = "Shirley"
age = 28
working_age = 5
lanuage = "Python"
method = "foramt"
print(f"{name} is now learning lanuage--{lanuage} and lear how to use method-{method}")
"""
"""
# format的特别用处
# 小数点位数
print("{0:.3f}" .format(1.0/3))
# 填满下划线
print("{0:_^11}" .format('hello'))
"""

"""
# break和continue的区别
while True:
    s = input("Enter something....:")
    if s == 'quit':
        break
    if len(s) < 3:
        print("Too small.")
        continue
    print("Input is of sufficient length")
"""

"""
# local variable / global variable
X = 50


def func():
    global X
    print("X is", X)
    X = 2
    print("Change global X to", X)
    # X = X + 1
    # print("X now value is", X)


func()
print("Value of X is", X)
"""

# *args **args

"""
def total(a=5, *numbers, **phonebook):
    print('a', a)

    for single_item in numbers:
        print('single_item', single_item)

    for first_part, second_part in phonebook.items():
        print(first_part, second_part)


total(10, 1, 2, 5, Jack=11223, John=2231, Inge=1560)
"""
"""
# 列表append、sort方法
shoplist = ['apple', 'mango', 'carrot', 'banana']
print("I have", len(shoplist), "items to purchase.")
print("These items are:", end=" ")   # end=" " 末尾不换行，加空格

for item in shoplist:
    print(item, end=" ")

print("\nI also have to bug rice.")  # 上一个print不换行输出，此处加一个换行符
shoplist.append("rice")              # 在列表的尾部添加rice
print("My shopping list is now", shoplist)

print("I will sort my list now")
shoplist.sort()                      # sort()方法--排序，默认升序排序，直接改变原列表
print("Sorted shopping list is", shoplist)

print("The first item I will buy is", shoplist[0])
olditem = shoplist[0]
del shoplist[0]                      # del 函数，删除列表的一个元素或是一系列
print("I bought the", olditem)
print("My shopping list is now", shoplist)
"""

"""
# 字典

ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Mastumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}


print("Swaroop's address is", ab['Swaroop'])

del ab['Spammer']

print('\nThere are {} contacts in the address-book\n' .format(len(ab)))

for name, address in ab.items():   # items()以列表形式返回可遍历的(key, value)元组数组
    print('Contact {} at {}' .format(name, address))

ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])

"""
"""
import os
import time
# 1. The files and directories to be backed up are
# specified in a list.
# Example on Windows:
source = ['E:\\Shirely\\Java']       # 打包原始文件夹
# Notice we have to use double quotes inside a string
# for names with spaces in it.  We could have also used
# a raw string by writing [r'C:\My Documents'].

# 2. The backup must be stored in a
# main backup directory. The directory named with the current date
# Example on Windows:
# target_dir = 'E:\\Backup'            # 打包存储目录
today = time.strftime('%Y%m%d')
target_dir = 'E:' + os.sep + today
# Remember to change this to which folder you will be using

# 3. The files are backed up into a zip file.
# 4. The name of the zip contain the current time and the comment from the input

commnet = input('Enter a comment-->')

if len(commnet) == 0:
    target = target_dir + os.sep + time.strftime('%H%M%S') + '.zip'        # os.seq 根据操作系统返回路径分隔符
else:
    target = target_dir + os.sep + commnet.replace(' ', '_') + time.strftime('%H%M%S') + '.zip'

# Create target dirctory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# 5.We use the zip command to put the files in a zip archive
zip_command = 'zip -r {0} {1}' .format(target, ' '.join(source))       # ' '.join() 连接字符串数组

# Run the backup
print('Zip command is :')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful back up to', target)
else:
    print('Backup FAILED')
"""

"""
try:
    text = input('Enter something --->')
except EOFError:
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:
    print('You cancelled the operation.')
else:
    print('You entered {}' .format(text))
"""

'''
class ShortInputExpection(Exception):
    """A user-defined exception class."""
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    text = input('Enter something -->')
    if len(text) < 3:
        raise ShortInputExpection(len(text), 3)
    # Other work can continue as usual here
except EOFError:
    print('Why did you do an EOF on me?')
except ShortInputExpection as ex:
    print(('ShortInputException: The input was ' + '{0} long, expected at least {1}') .format(ex.length, ex.atleast))
else:
    print('No exception was raised. ')

'''

# 询问名字，再询问年龄，再打印名字+年龄

question1 = input("请输入你的名字：")
question2 = input("请输入你的年龄：")
print("欢迎" + question1 + ",你今年" + question2 + ".")
