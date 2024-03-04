# Python program to count the number of digits in a number.

number = input("Enter the number: ")
count = 0
for i in range(1, len(number) + 1 ):
    count += 1

print("Count : ", count)