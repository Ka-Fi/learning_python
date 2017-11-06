import datetime

UserName = input("Give me your name: ")
print("Your name is " + UserName)
UserAge = int(input("Give me your age: "))
CurrentYear = datetime.datetime.now().year
TargetYear = 100 - UserAge + CurrentYear
Comm = str(UserName + ", you will be 100 years old in year " + str(TargetYear))
print(Comm)
n = int(input("How many times do you want to copy last message? "))
Comm2 = ""
for i in range(n):
    Comm2 = Comm2 + "\n" + Comm
print(Comm2)
