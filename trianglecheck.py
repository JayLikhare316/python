side1 = int(input("Enter the length of the first side: "))
side2 = int(input("Enter the length of the second side: "))
side3 = int(input("Enter the length of the third side: "))

if side1==side2==side3:
    print("It is an equilateral triangle.")
elif side1!=side2!=side3!=side1:
    print("It is a scalene triangle.")
else:
    print("It is a isoceles triangle.")
