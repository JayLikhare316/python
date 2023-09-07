num1 = 15
num2 = 26
num3 = 29

if num1 >= num2:
    if num2 >= num3:
        median = num2
    elif num1 <= num3:
        median = num1
    else:
        median = num3
else:
    if num1 >= num3:
        median = num1
    elif num2 <= num3:
        median = num2
    else:
        median = num3

print(median)
