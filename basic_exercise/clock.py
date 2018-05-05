#!/usr/bin/python3
import time 

# this is a alarm clock

def clock():
    hour = int(input('设定闹钟,小时:'))
    minute = int(input('设定闹钟,分钟:'))
    while True:
        t = time.localtime()
        pt = '\r%02d:%02d:%02d' % (t[3],t[4],t[5])
        print(pt,end='')
        if t[3] == hour and t[4] == minute:
            print()
            print('时间到')
            return
        time.sleep(1)
clock()
