print("Simple Quiz Game")
print()

score = 0

answer = input("1. What is the capital of India? ")

if answer.lower() == "new delhi":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("2. What is 2 + 2? ")

if answer == "4":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("3. Which language are we using? (Python/C++/Java) ")

if answer.lower() == "python":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print()
print("Your score is:", score, "/ 3")

if score == 3:
    print("Excellent!")
elif score == 2:
    print("Good!")
elif score == 1:
    print("Keep Practicing!")
else:
    print("Try Again!")