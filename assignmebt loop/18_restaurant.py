# 18. Challenge: Restaurant Ordering System.

total_bill = 0

while True:
    item = input("Enter item name (or 'done' to finish): ")

    if item == "done":
        break

    price = float(input("Enter item price: "))

    total_bill += price

print("\nTotal Bill =", total_bill)