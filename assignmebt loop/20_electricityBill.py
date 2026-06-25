# Challenge: Electricity Bill Generator.

while True:
    print("\n--- Electricity Bill Generator ---")
    print("1. Generate Bill")
    print("2. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        units = int(input("Enter units consumed: "))

        if units <= 100:
            bill = units * 5
        elif units <= 200:
            bill = units * 7
        else:
            bill = units * 10

        print("Electricity Bill = ", bill)

    elif choice == 2:
        print("Thank you!")
        break

    else:
        print("Invalid choice")