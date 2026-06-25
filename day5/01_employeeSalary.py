# Employee Salary Analysis
# Store salaries
# Find highest salary
# Find lowest salary
# Calculate average salary
# Count employees earning above average

# employee = {}

# calculate = False

# while calculate == False:
#     emp_name = input("enter the name of employee : ")
#     emp_salary = int(input("enter the salary amount : "))
#     # employee[enp_name]={"salary":emp_salary}
#     employee[emp_name] = emp_salary
#     print(employee)
#     nextStep=input("calculate or add next employee (y/n)")
#     if nextStep == "n":
#         print("a -> highest salary \nb -> lowest salary \nc -> avarage \nd ->above average")
#         calculateOption = input("select your option (a/b/c/d) : ")
#         if calculateOption == "a":
#             pass
#         elif calculateOption == "b":
#             pass
#         elif calculateOption == "c":
#             pass
#         elif calculateOption == "d":
#             pass
#     elif(nextStep == "y"):
#         pass
#     print(employee)
    
    


employee = {}

calculate = False

while calculate == False:
    emp_name = input("Enter the name of employee: ")
    emp_salary = int(input("Enter the salary amount: "))

    employee[emp_name] = emp_salary

    nextStep = input("Calculate or add next employee (y/n): ")

    if nextStep == "n":

        print("a -> highest salary")
        print("b -> lowest salary")
        print("c -> average")
        print("d -> above average")

        calculateOption = input("Select your option (a/b/c/d): ")

        if calculateOption == "a":
            highest = max(employee, key=employee.get)
            print("Highest salary employee:", highest, employee[highest])

        elif calculateOption == "b":
            lowest = min(employee, key=employee.get)
            print("Lowest salary employee:", lowest, employee[lowest])

        elif calculateOption == "c":
            avg = sum(employee.values()) / len(employee)
            print("Average salary:", avg)

        elif calculateOption == "d":
            avg = sum(employee.values()) / len(employee)

            print("Employees above average:")
            for name in employee:
                if employee[name] > avg:
                    print(name, employee[name])

        calculate = True

print(employee)