#!/usr/bin/python3

import time 

#This is a function to show you what is the time now

def show_time():
    while True:
        lt = time.localtime()
        s = '\r%02d:%02d:%02d' % lt[3:6]
        print(s)
        time.sleep(1)
show_time()
