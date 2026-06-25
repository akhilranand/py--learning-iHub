expenseBook = {}

def addExpense():
    print("\na -> Food")
    print("b -> Travel")
    print("c -> Shopping")

    category = input("Choose category: ")

    if category == "a":
        categoryName = "Food"
    elif category == "b":
        categoryName = "Travel"
    elif category == "c":
        categoryName = "Shopping"
    else:
        print("Invalid category")
        return

    month = int(input("Enter month (1-12): "))
    amount = float(input("Enter expense: "))

    if categoryName not in expenseBook:
        expenseBook[categoryName] = []

    expenseBook[categoryName].append(
        {"month": month, "amount": amount}
    )

    print("Expense Added")


def viewExpenses():
    for category in expenseBook:
        print("\n", category)

        for item in expenseBook[category]:
            print(item)


def totalSpending():
    total = 0

    for category in expenseBook:
        for item in expenseBook[category]:
            total += item["amount"]

    print("Total Spending =", total)


def highestExpense():
    highest = 0

    for category in expenseBook:
        for item in expenseBook[category]:
            if item["amount"] > highest:
                highest = item["amount"]

    print("Highest Expense =", highest)


def monthlyReport():
    month = int(input("Enter month: "))
    total = 0

    for category in expenseBook:
        for item in expenseBook[category]:
            if item["month"] == month:
                total += item["amount"]

    print("Month", month, "Expense =", total)


while True:

    print("\na -> Add Expense")
    print("b -> View Expenses")
    print("c -> Total Spending")
    print("d -> Highest Expense")
    print("e -> Monthly Report")
    print("f -> Exit")

    choice = input("Enter choice: ")

    if choice == "a":
        addExpense()

    elif choice == "b":
        viewExpenses()

    elif choice == "c":
        totalSpending()

    elif choice == "d":
        highestExpense()

    elif choice == "e":
        monthlyReport()

    elif choice == "f":
        break

    else:
        print("Invalid Choice")