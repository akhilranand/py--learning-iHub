# 4. Student Mark Entry System: Enter marks until -1 is entered; calculate total, average, and
# count.

total = 0
average = 0
count = 0
flag = False

while flag == False:
    
    mark = float(input("enter the mark : "))
    if mark != -1:
        count +=1
        total+=mark
        average = total/count
    if mark == -1:
        flag = True
print(".....................................")
print("coutn is : ",count)
print("the total mark is : ",total)
print("the average is : ",average)
print(".....................................")
