#!/sur/bin/python3
# 谁是小偷


# a说：小偷不是我
# b说：c是小偷
# c说：小偷肯定是d
# d说：c在冤枉人
# 3个人说了真话１个人说了假话

# 方法1
# 0 代表不是小偷 1代表是小偷
# m1/2/3/4分别代表abcd四个人话
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                m1 = a == 0
                m2 = c == 1
                m3 = d == 1
                m4 = d == 0
                if m1+m2+m3+m4 == 3 and a+b+c+d == 1:
                    print(a,b,c,d)
# 方法2
# 变量x代表小偷的代号
for x in range(chr('a'), chr('d')+1):
    t1 = x!=chr('a')
    t2 = x==chr('c')
    t3 = x==chr('d')
    t4 = x!=chr('d') 

