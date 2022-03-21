# @File : AMSTL.py
# @Author: minlu
# @Date : 2022/3/21
# @Desc :
# !/usr/bin/python3
# -*-conding:UTF-8-*-
# num = eval(input())
# gewei = num % 10
# shiwei = num //10 % 10
# baiwei = num // 100
# if gewei**3 + shiwei**3 + baiwei**3 == num:
#     print(str(num) + "是阿姆斯特朗数")
# else:
#     print(str(num) + "不是阿姆斯特朗数")
num = 0
num_list =[]
for number_test in range(100,1000):
    ge = number_test % 10
    shi = number_test // 10 % 10
    bai= number_test // 100
    if(ge ** 3 + shi ** 3 + bai ** 3 == number_test):
        num+=1
        #print(str(number_test) + "是阿姆斯特朗数")
        num_list.append(str(number_test))
print("100~1000 之间阿姆斯特朗数一共有:" + str(num))
print("100~1000 之间的阿姆斯特朗数分别是:" + str(num_list))
