unconfirmed_users = ["alice","brain","candace"]
confirmed_users = []
while unconfirmed_users:
    current_users = unconfirmed_users.pop()
    print("Verifying user: " + current_users.title())
    confirmed_users.append(current_users)
print("\n The following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#================== 函数列表形参 ====================================
def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
names = ['xiaomin','xiaoming','xiaohong']
greet_users(names)