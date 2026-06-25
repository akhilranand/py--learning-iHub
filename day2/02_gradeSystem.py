mark = float(input("Enter your mark : "))


if mark > 90:
    print("A")
elif mark >= 80 and mark <=90:
    print("B")
elif mark >=70 and mark < 80:
    print("C")
elif mark >= 60 and mark < 70:
    print("D")
elif mark >=50 and mark < 60:
    print("E") 
else:
    print("failed")   