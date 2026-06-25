# Guess the Number Game: Continue until the correct number is guessed.
magicNum = 7
while True:
    num = int(input("Enter the number : "))
    if(num == magicNum):
        print("wow the gussed number is correct")
        break
    else:
        print("sorry try again ")    
