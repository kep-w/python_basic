#!/usr/bin/python3
import random

# the str can be a password is like follow:
#     A-Z
#     a-z
#     0-9
#     '_'
# you can get a random passward consist by six string. 

l = ['0','1','2','3','4','5','6','_','7','8','9']
def lst(x,y):
    for x in range(x,y):
        l.append(chr(x))

lst(ord('A'),ord('Z')+1)
lst(ord('a'),ord('z')+1)

def mypsd(n):
    m = ''
    for x in range(6):
        m += random.choice(n)
    print(m)

mypsd(l)
