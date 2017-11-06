import random

rnd_num = str(random.randint(1000,9999))
print(rnd_num)
cow = 0
bull = 0
while cow != 4 and bull != 4:
    user_num = input("Give me 4-digit number")
    cow = 0
    bull = 0
    for i in range(3):
        if user_num[i] == rnd_num[i]:
            bull += 1
    for i in range(len(set(user_num))):
        if user_num[i] in rnd_num:
            cow += 1
    print("Cows : {}, Bulls : {}".format(cow, bull))

print("You right! Correct number is : ", rnd_num)
