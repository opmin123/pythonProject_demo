# @File : demo_learning_class.py
# @Author: minlu
# @Date : 2022/7/12
# @Desc :
# !/usr/bin/python3
# -*-conding:UTF-8-*-


class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def study(self,course_name):
        print('%s正在学习%s.'%(self.name,course_name))

    def watch_movie(self):
        if self.age < 18:
            print('%s看动画片.'%self.name)
        else:
            print('%s正在看书.'%(self.name))


def main():
    stu1 =Student('小明',25)
    stu1.study('Python程序设计')
    # 给对象发watch_av消息
    stu1.watch_movie()
    stu2 = Student('王大锤', 15)
    stu2.study('思想品德')
    stu2.watch_movie()



if __name__ == '__main__':
    main()
