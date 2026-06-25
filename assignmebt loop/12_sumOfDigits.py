# 12. Sum of Digits Application: Find sum, count, and reverse of digits.

num = int(input("Enter a number: "))

temp = num
sum_digits = 0
count = 0
reverse = 0

while temp > 0:
    digit = temp % 10
    sum_digits += digit
    count += 1
    reverse = reverse * 10 + digit
    temp //= 10

print("Sum of digits:", sum_digits)
print("Count of digits:", count)
print("Reverse of number:", reverse)
