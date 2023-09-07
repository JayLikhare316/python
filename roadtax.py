price = int(input("Enter the cost price of the bike (in Rs): "))

if price > 100000:
    taxpercentage = 15
elif price > 50000:
    taxpercentage = 10
else:
    taxpercentage = 5

roadtax = (price * taxpercentage) / 100

print(f"Road tax to be paid: Rs {roadtax}")
