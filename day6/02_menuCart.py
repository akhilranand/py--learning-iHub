# Food Ordering System

menu = {
    "Burger": 120,
    "Pizza": 250,
    "Shawarma": 180,
    "Juice": 60
}

cart = []
order_history = []


def viewMenu():
    print("\n----- MENU -----")
    for item, price in menu.items():
        print(f"{item} : ₹{price}")


def addFood():
    item = input("Enter food item: ")

    if item in menu:
        qty = int(input("Enter quantity: "))

        cart.append({
            "item": item,
            "qty": qty,
            "price": menu[item]
        })

        print("Item added to cart")
    else:
        print("Food item not found")


def removeFood():
    item = input("Enter item to remove: ")

    for food in cart:
        if food["item"] == item:
            cart.remove(food)
            print("Item removed from cart")
            return

    print("Item not found in cart")


def viewCart():
    if len(cart) == 0:
        print("Cart is empty")
        return

    print("\n----- CART -----")
    for food in cart:
        subtotal = food["qty"] * food["price"]
        print(
            f'{food["item"]} | Qty: {food["qty"]} | '
            f'Price: ₹{food["price"]} | Subtotal: ₹{subtotal}'
        )


def bill():
    if len(cart) == 0:
        print("Cart is empty")
        return

    total = 0

    print("\n----- BILL -----")
    for food in cart:
        subtotal = food["qty"] * food["price"]
        total += subtotal

        print(
            f'{food["item"]} | Qty: {food["qty"]} | '
            f'Price: ₹{food["price"]} | Subtotal: ₹{subtotal}'
        )

    print(f"\nTotal Bill = ₹{total}")

    order_history.append(cart.copy())
    cart.clear()


def orderHistory():
    if len(order_history) == 0:
        print("No orders yet")
        return

    print("\n----- ORDER HISTORY -----")

    for order_no, order in enumerate(order_history, start=1):
        print(f"\nOrder {order_no}")

        for food in order:
            print(
                f'{food["item"]} | Qty: {food["qty"]}'
            )


while True:

    print("\n1. View Menu")
    print("2. Add Food Item")
    print("3. Remove Food Item")
    print("4. View Cart")
    print("5. Generate Bill")
    print("6. Order History")
    print("7. Exit")

    action = input("Enter your option (1-7): ")

    if action == "1":
        viewMenu()

    elif action == "2":
        addFood()

    elif action == "3":
        removeFood()

    elif action == "4":
        viewCart()

    elif action == "5":
        bill()

    elif action == "6":
        orderHistory()

    elif action == "7":
        print("Thank you!")
        break

    else:
        print("Invalid option")