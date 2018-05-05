#!/usr/bin/python3
# 练习：
# 1.算出100到999以内的水仙花数(Narcissistic Number)
#  (水仙花数是值百位的3次方加上十位的3次方加上各位的3次方等于原数的数字)
# 例如： 153 等于 1**3 + 5**3 + 3**3

# 方法1
for x in range(1,10):
    for y in range(10):
        for z in range(10):
            n = x*100 + y *10 + z
            if x **3 + y **3 + z**3 == n:
                print('100到999以内的水仙花有：', n)
# 方法2
for x in range(100,1000):
    a = x//100
    b = x%100//10
    c = x % 10
    if a**3 + b**3 + c**3 == x:
        print('100到999以内的水仙花有：', x)
# 方法3
for x in range(100, 1000):
    a = int(str(x)[0])
    b = int(str(x)[1])
    c = int(str(x)[2])
    if a**3 + b**3 + c**3 == x:
        print('100到999以内的水仙花有：', x)
