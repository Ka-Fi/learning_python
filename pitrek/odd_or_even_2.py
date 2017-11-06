Number = int(input("Give me your number: "))
Divider = int(input("Give me your divider: "))
Rest = (Number % Divider)
if int(Rest) == 0:
    print("Even")
else:
    print("Odd")