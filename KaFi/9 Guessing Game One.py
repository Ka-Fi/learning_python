import random

a = random.randint(0,9)
x = int(input("give me a number between 1 and 9"))
print("random numer is ", a)
if a == x :
    print("You right!")
elif a<x :
    print("to high")
else:
    print("to less")
