import random
def generator_mark():
    marks = "!@#$%^&*.,"
    return marks[random.randint(0,9)]

def generator_number():
    marks = "0123456789"
    return marks[random.randint(0,9)]

def generator_letter():
    marks = "qwertyuiopasdfghjklzxcvbnm"
    return marks[random.randint(0,26)]

def generator_big_letter():
    marks = "QWERTYUIOPASDFGHJKLZXCVBNM"
    return marks[random.randint(0,26)]

def generator():
    i = random.randint(0,3)
    if i == 0:
        rnd = generator_mark()
    elif i == 1:
        rnd = generator_number()
    elif i == 2:
        rnd  = generator_letter()
    else:
        rnd = generator_big_letter()
    return rnd

def password_gen():
    number = 1 + int(input("Length of password"))
    password = []
    for i in range(number):
        password.append(generator())

    print("".join(password))

password_gen()