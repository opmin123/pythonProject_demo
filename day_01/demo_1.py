#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/7/9 13:50 
# @Author : minlu
# @Version：V 0.1
# @File : demo_1.py

#变量的类型和使用;type 关键字线上python 变量的所属类型
a = 4
b = 2
c = "123456"
d = 8.3
e = int(d)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(e)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

#%d,%f,占位符
#num_1 = int(input("num_1 = "))
#num_2 = int(input("num_2 = "))
#print("%d + %d = %d"%(num_1,num_2,num_1 + num_2))

num_3 = 10
num_4 = 3
num_3 +=num_4
print(num_3)
num_3 *=num_3 + 2
print(num_3)

#华氏温度转换为摄氏温度
f = float(input("请输入华氏温度:"))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f 摄氏度' %(f,c))
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')

#技术圆的周长和面积
r = float(input('请输入圆的半径:'))
ZC = r*3.14*2
MJ = 3.14 *r*r
print('周长是:%.2f'%ZC)
print('面积是:%.2f'%MJ)

#判断输入的年份是否是润年,润年输出True 否则输出 false
year = int(input("请输入年份:"))

is_leap =year % 4 == 0 and year % 100 !=0 or year % 400 ==0
print(is_leap)