#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/7/10 10:56 
# @Author : minlu
# @Version：V 0.1
# @File : demo_3_trangle.py



#打印不同的*三角图案
#右边
row = int(input('请输入行数:'))
for i in range(row):
    for j in range(i+1):
        print('*',end=' ')
    print()


#左边打印
for i in range(row):
    for j in range(row):
        if j < row -i - 1:
            print(' ',end=' ')
        else:
            print('*',end= ' ')
    print()


#打印完整
for i in range(row):
    for j in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()