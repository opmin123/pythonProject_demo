#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/7/9 16:02 
# @Author : minlu
# @Version：V 0.1
# @File : demo_3_for.py


# 输出九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()