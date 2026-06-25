# 13. Inventory Management: Add product quantities and calculate total stock.
total_stock = 0

while True:
    product = input("Enter product name (or stop to exit): ")

    if product == "stop":
        break

    quantity = int(input("Enter quantity: "))

    total_stock += quantity

print("\nTotal Stock:", total_stock)