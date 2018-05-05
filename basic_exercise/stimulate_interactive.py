#!/usr/bin/python3

# This is a function, it stimulate the python interactive

g = {}
l = {}
def mypro():
    while True:
        s = input('>>>')
        if s == 'bye':
            break
        exec(s, g, l)

mypro()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          