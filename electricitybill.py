unitconsumed = int(input("Enter the number of units consumed: "))

unit_price_1 = 0  # First 100 units
unit_price_2 = 5  # Next 100 units
unit_price_3 = 10  # Units above 200

total_bill = 0

if unitconsumed <= 100:
    total_bill = unitconsumed * unit_price_1
elif unitconsumed <= 200:
    total_bill = 100 * unit_price_1 + (unitconsumed - 100) * unit_price_2
else:
    total_bill = 100 * unit_price_1 + 100 * unit_price_2 + (unitconsumed - 200) * unit_price_3

print(f"The total bill amount is Rs{total_bill}")
