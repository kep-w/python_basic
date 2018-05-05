#!/usr/bin/python3
import random

def alst():
    al =[]
    l1 = ['\u2660', '\u2663', '\u2665','\u2666']
    l2 = ['A', 'J', 'Q', 'K', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    for x in range(4):
        for y in l2:
            al.append(l1[x]+' '+ y)
    al.append('Big Joker')
    al.append('Little Joker')
    return al

def deal():
    al = alst()
    for x in range(3):
        input('点击<回车>发牌给第%d个人' % (x+1))
        card = random<.s>ample(al, 17)
        for x in card:
            print('|-', x, '-|', end='')
            al.remove(x)
        print()

    input('点击<回车>亮底牌')
    print('|-',al[0],'-|-',al[1],'-|-',al[2],'-|')

deal()


