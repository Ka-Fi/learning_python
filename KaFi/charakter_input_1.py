name = input("Give me your name : ")
age = input("How old are u?")
number = input("What is your favourite number ? ")
for i in range(int(number)):
    print(i+1 ,". ", name, ", Person who are 100 years old than you is : ", int(age)+100)

print(int(number)*("Your name is " + name + "\n"))