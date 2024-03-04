# Python program to find the sum of digits in a number.

number = (input("Enter number : "))
sum = 0 
for i in range(1, len(number) + 1 ):
    i = int(i)
    sum = sum + i
print("Sum of Digits : ",sum)
