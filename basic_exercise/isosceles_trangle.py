#!/usr/bin/python3

# input a number then print a '*' isosceles trangle
#           *    
#          ***   
#         *****  
#        *******        
#       *********
n = int(input('输入一个整数：'))
i = 1
while i <= n:
    print(('*'*(2*i-1)).center(2*n-1))
    i += 1
print('----------------------')

for x in range(1, n+1):
    print((n-x)*' '+ (2*x-1)*'*')