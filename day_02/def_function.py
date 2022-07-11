# @File : def_function.py
# @Author: minlu
# @Date : 2022/7/11
# @Desc :
# !/usr/bin/python3
# -*-conding:UTF-8-*-



#def 定义python函数关键字
#输入m,n,求C(m,n)
def fac(num):
    result = 1
    for n in range(1,num + 1):
        result *=n
    return result

m = int(input(' m = '))
n = int(input( ' n = '))
print(fac(m) // fac(n) // fac(m-n))

