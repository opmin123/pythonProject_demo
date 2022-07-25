# @File : class_test.py
# @Author: minlu
# @Date : 2022/7/25
# @Desc :
# !/usr/bin/python3
# -*-conding:UTF-8-*-

#验证python 私有和公有属性

class Test:
    def __init__(self,foo):
        self.__foo = foo #双下划线私有属性
    def __bar(self): #私有方法
        print(self.__foo)
        print('__bar')


def main():
    test =Test("Hello")
    test._Test__bar()
    print(test._Test__foo)
if __name__ == "__main__":
    main()
