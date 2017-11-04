

def check_primarity():
    try:
        number = int(input("Give me a numer : "))
    except ValueError:
        return ("You don't give a number")
    if number == 0 or number == 1:
        return "this is not prime number and not compound number"
    elif number == 2:
        return ("this is prime number")
    else:
        for i in range(2,number):
            if number % i == 0:
                return ("this is compound number")
            else:
                return("this is prime number")

print(check_primarity())