#！\usr\bin\python3
#author:kepner
#date:2018.04.12

#让用户输入要计算的时间：
year = int(input('输入年：'))
month = int(input('输入月：'))
day = int(input('输入日：'))
#将一年中每个月1号相对已过去的天数计算出来放到元组中
months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335]
#过去的日子和还剩下的日子都不包含当天
days = -1
l_day = 365-1
if month in range(1, 13):
    days += months[month-1]
else:
    print('输入错误')
days += day
#闰年且输入月份大于3时需考虑多加一天：
if year % 4 == 0 and year%100!=0:
    if months>3:
        days+=1
        l_day+=1
if year % 400 == 0:
    if months>3:
        days+=1
        l_day+=1
l_day -= days
if l_day<0:
    l_day = 0
print('%d已经过去了: %d天' % (year,days))
print('%d还剩下%d天' % (year, l_day))