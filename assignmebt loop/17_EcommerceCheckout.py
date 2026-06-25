# Challenge: E-Commerce Checkout.
total = 0

while True:
    price = input("Enter product price (or 'checkout' to finish): ")

    if price == "checkout":
        break

    total += float(price)

print("Total Bill =", total)