

exit = False
while exit == False:
    print("a -> Deposite")
    print("b -> withdraw")
    print("c -> exit")
    option = input(("chose an option : "))
    if option == 'a' :
        print("          ----Deposite success----")
    elif option == 'b':
        print("          ----withdraw success----")
    else:
        print("          ----Exit Thank you----")
        exit = True;        

