#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/7/9 16:02 
# @Author : minlu
# @Version：V 0.1
# @File : demo_3_for.py


# 输出九九乘法表
from math import sqrt

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()

#输入一个数判断是否为素数

num = int(input("请输入一个整数:"))
end = int(sqrt(num))
is_prime = True
for x in range(2,end +1):
    if num % x ==0:
        is_prime = False
        break
if is_prime and num !=1:
    print('%d 是素数' % num)
else:
    print('%d 不是素数'% num)


#求最大公约数和最小公倍数
x = int(input('x = '))
y = int(input('y = '))
if x > y :
    x , y = y , x
for factor in range(x , 0 , -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d 的最大公约数是%d' %(x,y,factor))
        print('%d 和%d 的最小公倍数是%d' %(x,y,x*y//factor))
        break