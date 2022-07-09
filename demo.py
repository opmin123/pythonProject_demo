#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/3/6 15:03 
# @Author : minlu
# @Version：V 0.1
# @File : demo.py
import sys
print("路径为:%s"% sys.path)


name={'小米':'3999','华为':'none','苹果':'none','三星':'none'}
info=dict.fromkeys(name)
print(info)
print(info.items())
print(info.keys())
print(name.setdefault('小米'))
print(name.get('小米'))
print(name.values())
student={'小米':'1001','小胡':'1002','小张':'1003','小红':'1004'}
print("小米的学号是: %-10s"% student.get('小米'))
