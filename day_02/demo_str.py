# @File : demo_str.py
# @Author: minlu
# @Date : 2022/7/11
# @Desc :
# !/usr/bin/python3
# -*-conding:UTF-8-*-


# s1 = '\'hello world\''
# s2 = '\n\\hello world\\\n'
# s3 ="""
# hello,
# world
# """
#
# s4 ='hello' *3
# print('s4 的值是: ',s4)
# print(s1,s2,end='')
#
# str2 = 'abc123456'
# print(str2[2])
# #print(str2[2:6])
# print(str2[2::3])
#
# list1 = [1,3,5,7,100]
# for elm in list1:
#     print(elm)
#
#
# for index,element in enumerate(list1):
#     print(index,element)
import os
import time


def main():
    content = '北京欢迎你为你开天辟地.....'
    while True:
        os.system('cls')
        print(content)
        time.sleep(1)
        content = content[1:] + content[0]



if __name__ =='__main__':
    main()