#!\usr\bin\python3
# author:kepner
# date:2018.04.12
# 计算出20个斐波那契数（fabonacci）的两种方法

# method 1
# 定义一个空的列表用于存放计算出的数
l = [1, 1]   # 创建一个列表，包含前两个没有规律的数
for x in range(18):   # 循环18次，依次将从第三个数起的所有数字添加进列表
    l.append(l[-1]+l[-2])   # 每个数等于前两个数的和
print(l)

# method 2:
l2 = [] 
i = 1   # 作为第一个数
j = 1   # 作为第二个数
l.append(i)   
l.append(j)
for x in range(18):    # 循环18次，依次将从第三个数起的所有数字添加进列表
    l2.append(i+j)     # 每个数等于前两个数的和
    i, j = j, i+j
print(l2)
