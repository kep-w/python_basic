#!/usr/bin/python3
# perfect number is the number like 6, that:
#     1+2+3 = 6
#     1*6 = 6
#     2*3 = 6
# print perfect numbers less than 10000:


#把一个数的所有除了本身以外的因数相加如果等于这个数，即为完美数

for x in range(1,10000):
    perfect = 0
    for y in range(1,x):
        if x % y == 0:
            perfect += y 
    if x == perfect:
        print(x)
