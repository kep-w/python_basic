#!/usr/bin/python3
import time 

# input your birthday,the function will tell you what day it is, and how many days you have spend in the earth 
def birthday():
    year = int(input('请输入你的出生年:'))
    month = int(input('请输入你的出生月:'))
    day = int(input('请输入你的出生日:'))
    mt = time.mktime((year, month, day,0,0,0,0,0,0))
    lt = time.localtime(mt)
    l = ['星期一',
         '星期二',
         '星期三',
         '星期四',
         '星期五',
         '星期六',
         '星期日']
    print(l[lt[6]])
    days = (time.time()-mt)//(3600*24)
    print('今天是你在地球上第 %d 天' % days)

birthday()
