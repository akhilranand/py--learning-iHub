# 8. Library Book Issue System: Issue books and update stock.


totalbooks = 5

while True:
    book = input("Do you want a Book  (y/n) : ")
    if totalbooks > 0:
        if book == "y" :
            totalbooks -= 1
            print("Thank you")
        else:
            print("Exit")
            break     
    else:
        print("book not available ")  
        break      