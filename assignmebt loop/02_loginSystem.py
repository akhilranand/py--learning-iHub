# 2. Login System: Allow 3 attempts to enter the correct password.

savedPassword = "abc123"
count = 0

while count <3:
    password = input("enter your password : ")
    if savedPassword == password:
        print("login success.")
        count = 3
    else:
        count +=1
        print("count is ",count)
        print("wrong password...")
        if(count == 3):
            print("sorry 3 attempts failed try after 24 hours........")    