#!\usr\bin\python3
# author:kepner
# date:2018.04.12
#Python中素数的验证方法:

# 1.输入一个数字，将从1到这个数字中间的所有素数找出来

n = int(input('输入一个整数：'))
# 方法1：
l = [x for x in range(2,n+1) if not [y for y in range(2,x) if x % y == 0]]
print(l)
# 方法2：
l1 = []
for x in range(2, n):
    for y in range(2, x):
        if x % y == 0:
            break
    else:
        l1.append(x)
print(l1)

# 2.输入一个数字，验证这个数字是不是素数：
_prime = int(input('输入一个整数：'))
if _prime <= 1:
    print(_prime, '不是素数')
else:
    for x in range(2, _prime):
        if _prime % x == 0:
            print(_prime, '不是素数')
            break
    else:
        print(_prime, '是素数')

