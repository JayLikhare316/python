quantity = int(input("Enter the quantity of items: "))
unitcost = 100
totalcost = quantity * unitcost

if totalcost > 1000:
    discount = 0.10 * totalcost
    totalcost -= discount

print(f"Total cost: Rs.{totalcost}")
