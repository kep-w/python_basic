# 1、有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 程序分析：可填在百位w、十位、个位的数字都是1、2、3、4。
# 组成所有的排列后再去 掉不满足条件的排列。

l = []
for x in range(1,5):
    for y in range(1,5):
        for z in range(1,5):
            a_re = x*100 + y*10 +z
            if x != y and x != z and y != z:
                l.append(a_re)

print('能组成%d个无重复的数字，他们是：'%len(l))
print(l)