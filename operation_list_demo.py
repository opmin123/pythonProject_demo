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