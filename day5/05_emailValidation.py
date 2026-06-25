def mailValidation(eMail):
    if "@gmail.com" in eMail:
        if " " in eMail:
            print ("sorry not valid")
        print ("yes its valid")
    else:
        print("sorry not valid")    
mailValidation("ab@gmail.com")