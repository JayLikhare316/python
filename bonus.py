salary = float(input("Enter your salary: Rs."))
yearsofservice = int(input("Enter your years of service: "))

if yearsofservice >= 5:
    bonus = 0.05 * salary
    print(f"Your bonus is Rs.{bonus}")
else:
    print("Sorry, you are not eligible for a bonus.")

