#!/usr/bin/python3

# input a number then print a number isosceles trangle
# like this:
#    1
#   121
#  12321
# 1234321

n = int(input('输入一个大于0的整数：'))

for x in range(1,n+1):
    s = ''
    for y in range(1,x+1):
        s += str(y)
    s1 = s[:-1]
    s2 = s1[::-1]
    print((s+s2).center(2*n-1))
