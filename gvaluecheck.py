num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

if num1 > num2:
    print(f"The greatest number is {num1}.")
elif num2 > num1:
    print(f"The greatest number is {num2}.")
else:
    print("Both numbers are equal.")