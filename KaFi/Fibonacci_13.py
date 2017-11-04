import numpy as np


def Fibonacci():
    try:
        number = int(input("Give me a numer : "))
    except ValueError:
        return ("You don't give a number")
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        arr = np.arange(number+1)
        for i in range(2,number+1):
            print(i)
            arr[i]=arr[i-1]+arr[i-2]
        return arr

print(Fibonacci())