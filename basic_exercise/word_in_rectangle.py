#!/usr/bin/python3

# input 3 lines words then print like this:
#         +-------------------------------+
#         |         hello rarena!         |
#         |       my name is kepenr.      |
#         |        today is sunday!       |
#         +-------------------------------+
#     注：max() 函数可以输入多个参数，最终返回最大的一个
s1 = input('输入1')
s2 = input('输入2')
s3 = input('输入3')
m = max(len(s1),len(s2),len(s3))
print('+' + '-'*(m+2) + '+')
print('|'+ ((m+2-len(s1))//2)*' ' + s1 + ((m+2-len(s1))-(m+2-len(s1))//2)*' '+'|')
print('|'+ ((m+2-len(s2))//2)*' ' + s2 + ((m+2-len(s2))-(m+2-len(s2))//2)*' '+'|')
print('|'+ ((m+2-len(s3))//2)*' ' + s3 + ((m+2-len(s3))-(m+2-len(s3))//2)*' '+'|')
print('+' + '-'*(m+2) + '+')
