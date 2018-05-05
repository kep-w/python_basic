#!/usr/bin/python3

# input a number then print a '*' Christmas tree
# like this: 
#      *
#     ***
#    *****
#   *******
#  *********
# ***********
#      *         
#      *         
#      *         
#      *         
#      *         
#      *         

n = int(input('输入一个整数：')) 

for i in range(0,n+1):
    print(' '*(n-i)+ (2*i-1)*'*')
else:
    for x in range(n):
        print('*'.center(2*n-1))

# then change the code to print a number Christmas tree
# like this:
# (the placeholder of the number above 10 is two byte, and the number for 0 to 9 is one.
# so, print this kind of tree, you need input the number less than 10)
#    1
#   222
#  33333
# 4444444
#    #   
#    #   
#    #   
#    # 

for i in range(0,n+1):
    print(' '*(n-i)+ (2*i-1)*str(i))
else:
    for x in range(n):
        print('#'.center(2*n-1))