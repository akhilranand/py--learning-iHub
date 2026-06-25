inventory = {
    "pen": 50,
    "notebook": 30,
    "eraser": 100
}

while True:

    print("\nCurrent Inventory:")
    for item in inventory:
        if inventory[item] == 0:
            print(item, "= Out of Stock")
        else:
            print(item, "=", inventory[item])

    print("a -> Add stock")
    print("b -> Buy item")
    print("c -> Check out-of-stock items")
    print("d -> Find item with highest stock")
    print("e -> Exit")

    action = input("Your option (a/b/c/d/e): ")

    # Add stock
    if action == "a":
        item = input("Which item do you want to update? ")
        qty = int(input("Enter quantity to add: "))
        inventory[item] = inventory[item] + qty

    # Buy item
    elif action == "b":
        item = input("Which item do you want to buy? ")
        qty = int(input("Enter quantity: "))

        if qty <= inventory[item]:
            inventory[item] = inventory[item] - qty
            print("Purchase successful")
        else:
            print("Not enough stock")

    # Check out-of-stock items
    elif action == "c":
        print("Out of Stock Items:")
        for item in inventory:
            if inventory[item] == 0:
                print(item)

    # Highest stock item
    elif action == "d":
        highest_item = ""
        highest_qty = 0

        for item in inventory:
            if inventory[item] > highest_qty:
                highest_qty = inventory[item]
                highest_item = item

        print("Highest stock item:")
        print(highest_item, "=", highest_qty)

    # Exit
    elif action == "e":
        print("Goodbye!")
        break

    else:
        print("Invalid option")