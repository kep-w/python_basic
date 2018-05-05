#!/usr/bin/python3

# input a number then print a number square.
# like this: 
#         如：输入：5
#         1 2 3 4 5
#         2 3 4 5 6
#         3 4 5 6 7
#         4 5 6 7 8
#         5 6 7 8 9
#         输入3：
#         1 2 3
#         2 3 4 
#         3 4 5
# method 1
n = int(input('输入一个整数：'))
i = 1
while  i <= n:
    j = 0
    while j < n:
        print(j+i, end='')
        j += 1
    print()
    i += 1

print('======I am a separator line======')

# method 2
for x in range(1, n+1):
    for j in range(x,n+x):
        print(j, end='')
    print()