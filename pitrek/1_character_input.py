import datetime

UserName = input("Give me your name: ")
print("Your name is " + UserName)
UserAge = int(input("Give me your age: "))
CurrentYear = datetime.datetime.now().year
TargetYear = 100 - UserAge + CurrentYear
UserName + ", you will be 100 years old in year " + str(TargetYear)
