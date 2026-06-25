#  Attendance Management System: Mark students Present/Absent until stop is entered.

present = 0
absent = 0

while True:
    status = input("Enter attendance (Present/Absent) or Stop to exit: ")

    if status == "stop":
        break

    elif status== "p":
        present += 1

    elif status == "a":
        absent += 1

    else:
        print("Invalid input")

print("Attendance Summary")
print("Present:", present)
print("Absent:", absent)