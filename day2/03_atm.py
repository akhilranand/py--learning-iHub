balance = 10
pin = 1456


pinNum = int(input("Enter your number : "))
if pin == pinNum:
    print("Welcome ")
    print(" a -> Balance ")
    print(" b -> Withdraaw ")
    print(" c -> Deposite ")


    action = input("Enter your selection : ")

    if action == "a":
        print("your balance is ",balance)
    elif action == "b":
        withdrawAmount = float(input("Enter the amount you want to withdraw : "))
        if withdrawAmount > balance :
            print("sorry insufficent balance")
        else:
            balance -= withdrawAmount
            print("your balance is ",balance)
    elif action == "c":
        depositeAmount = float(input("enter the amount you want to deposite : "))
        balance+=depositeAmount
        print("Your balance is ",balance)     
    else:
        print("invalid action")    



else:
    print("Sorry wrong pin")
