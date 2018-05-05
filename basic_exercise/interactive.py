#! /usr/bin/python3

# author:kepner
# date:2018.04.18

# a simple python3 interactive simulation

g = {}
l = {}

while True:
    s = input('>>>')
    if s == 'exit()':
        break
    exec(s, g, l)

# if you need, this statement can print the variable you have created.
print('您刚刚创建的变量有:', l)