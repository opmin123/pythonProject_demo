#aurhor minlu
#date 2022-1-17
#操作列表demo
magicians = ['alice','david','carolina']
for mag in magicians:
  print(mag.title() + ",that was a great tricek")
#demo2
print("=================================== 第二个demo ==================================")
pizzas = ['pizz_1','pizz_2','pizz_3']
for pizza in pizzas:
    print(pizza + ',I like pepperoni pizza!')
print("I really love pizza!")
#======================================= 创建数直列表 ====================================
for num in range(1,5):
    print(num)

even_num = list(range(2,11,2))
print(even_num)

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)
#++++++++++++++++++++++++++++++++++++++++ 第二种方式 列表解析 +++++++++++++++++++++++++++++++++++++
squares = [value**2 for value in range(1,11)]
print(squares)




#========================== for循环打印1~20 的数字 ==========================================
squares_2 = [nu for nu in range(1,21)]
print("squares_2的值是:", squares_2)
for nu in range(1,21):
    print(nu)


#============================= 计算1~10000的总和 ===========================================
squares_3 = [nu for nu in range(1,10001)]
sum = 0
for squares_valu in squares_3:
    sum = sum + squares_valu

print("squares_3 的最大值是:",max(squares_3))
print("squares_3 的最小值是:",min(squares_3))
print("1~10000的总和是:",str(sum))

#============================== 给range()指定三个参数，包含1~20的奇数，并打印这些奇数 ============
#num_list = [(js_num*2-1) for js_num in range(1,20)]
#print(num_list)
for js_num in range(1,20,2):
    print(js_num)

#=========================================================== 切片技术 ========================
colors = ['red','blue','green','yellow','black']
print(colors[0:3])#结果:red,blue,green
print(colors[1:3])#结果:blue,green
print(colors[:3])#结果:red,blue,gree
print(colors[2:])#结果:green,yellow,blcak
print(colors[:-2])#结果:'red', 'blue', 'green'
print(colors[-2:])#结果:'yellow', 'black

#================================================ 遍历切片 ===================================
for color in colors[:3]:
    print(color.title())#red,blue,green
#================================================ 复制列表 ==================================
my_foods = ['pizza','falafel','carrot cake']
#friend_foods = my_foods
friend_foods = my_foods[:]
print(friend_foods)
my_foods.append('ice cream')
friend_foods.append("cannoli")
print(friend_foods)
print(my_foods)
#================================================ 元组 =====================================
#元组的值是不能修改的,但是可以给整个元组重新复制
distmeno = (10,20)
print(distmeno[0])
#distmeno[0]=30//错误,不能修改元组的值
print(distmeno[0])

#================================================ python if 语句 ==========================
cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper()) #相等所有字母大写
    else:
        print(car.title())#否则首字母大写

#=============================================== if-elif-else ===========================
age = 18
if age < 15:
    print("your admission cost is $0.")
elif age < 18:
    print("your admission cost $5.")
else:
    print("your admission cost is $10.")

#============================================== 字典 ===================================
aline = {'color':'green','points':'23'}
print(aline['color'])
#=========================================== 2022-1-21 字典循环 ==================================
favorite_lanaguages = {'jen':'python','sarah':'c','edward':'ruby','phil':'python'}
print("Sarah`s favorite language is " + favorite_lanaguages['sarah'].title() + '.')
for key , value in favorite_lanaguages.items():
    print("\nKey:" + key)
    print("Value:" + value)
for name , language in favorite_lanaguages.items():
    print(name.title() + "`s favorite language is " + language.title() + ".")
#=========================================== 字典列表 ============================================
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}
aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)
#=========================================== python 用户输入 ====================================
age = input("hellow old are youage ")