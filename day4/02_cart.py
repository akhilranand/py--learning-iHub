# Shopping Cart (List + Dictionary)
# Add items
# Remove items
# Calculate total bill

exit  = False
total = 0
myCart = {}
while exit == False:
    print("a -> add item \nb -> remove item \nc -> calculate total")
    action = input("enter your choise : ")
    if action == "a":
        item = input("enter the iten you need to add : ")
        qty = int(input("enter the qty of item you need : "))
        myCart[item] = qty
        print(myCart)
    elif action == "b":
        item = input("enter the iten you need to remove : ")
        myCart.pop(item)
        print("item has been removed from the list")
        print(myCart)
    elif action == "c":
        for item in myCart:
            total = total + myCart[item]
        print("the total bill is : ",total)   

    
