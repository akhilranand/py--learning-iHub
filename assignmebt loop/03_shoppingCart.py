# 3. Shopping Cart: Enter product prices until 0 is entered and calculate total bill.
sum = 0
flag = False

while flag == False:
    cart = float(input("enter the amount : "))
    sum+=cart
    if(cart == 0 ):
        print("          ----Exit----")
        flag = True
print ("the total amount is ",sum)        

