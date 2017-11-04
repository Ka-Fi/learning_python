number = int(input("Give me a number"))
x = []
for i in range(1, number+1):
    if number % i == 0:
        x.append(i)

print("Divisors number {} is {}".format(number, x))