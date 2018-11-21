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


def total(a=5, *numbers, **phonebook):
    print('a', a)

    for single_item in numbers:
        print('single_item', single_item)

    for first_part, second_part in phonebook.items():
        print(first_part, second_part)


total(10, 1, 2, 5, Jack=11223, John=2231, Inge=1560)



