# Calculate total expenses.
# Find the highest expense.
# Find the lowest expense.
cart = []
totalIterm = 5
for i in range(5):
    expence = float(input("enter the amount : "))
    cart.append(expence)
print(cart)    

print("total expenses" ,sum(cart))
print("highest expense" ,max(cart))
print("lowest expense" ,min(cart))

