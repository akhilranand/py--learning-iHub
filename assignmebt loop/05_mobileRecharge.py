# 5. Mobile Recharge Menu: Create a menu-driven recharge application.

while True:
    print("--- Mobile Recharge Menu ---")
    print("1. Recharge ₹99")
    print("2. Recharge ₹199")
    print("3. Recharge ₹299")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("₹99 Recharge Successful")
    elif choice == 2:
        print("₹199 Recharge Successful")
    elif choice == 3:
        print("₹299 Recharge Successful")
    elif choice == 4:
        print("Thank you. Exiting...")
        break
    else:
        print("Invalid Choice")