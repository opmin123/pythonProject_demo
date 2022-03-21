# @File : study_demo.py
# @Author: minlu
# @Date : 2022/3/1
# @Desc :

number = ['a','b','c','d','e','f','g','h','i','j']
print(number[2:3:3]) #c
print(number[2:3:4]) #c
print(number[2:3:5]) #c
print(number[2:4:2]) #c
print(number[2:4:1]) #c,d
print(number[2:4:-1]) #[]
print(number[2:0:-2]) #c,e,g,i
number.remove('a')
print(number)
print(1,2,3)
student={'小华':['1002',23,'男'],'小张':'1003','小红':'1004','小浩':'1005'}
print(student['小浩'])
#student.clear()
print(student)

student_copy=student.copy()
print("复制:",student_copy)
student_copy['小华'].remove('1002')
print('new',student_copy)
print('old',student)


#============================ 替换========================
student_copy['小红']='1009'
print(student_copy)
print(student)
print(student_copy.get('小明'))
print(student_copy.keys())