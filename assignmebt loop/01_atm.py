# 1. ATM Withdrawal System: Withdraw repeatedly until balance becomes 0 or user exits.
balance = 12544

while balance > 0:
    print("your balance", balance)
    amount = float(input("enter the amount to be withdrawn: "))
    
    if amount > balance:
        print("sorry insufficient balance")
    else:
        balance -= amount
        print("now your current balance is", balance)