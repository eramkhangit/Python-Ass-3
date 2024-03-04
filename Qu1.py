# Python program to calculate factorial of a given number.

number = int(input("Enter number : "))
factorial = 1
for i in range( 1, number + 1 ):
    factorial = factorial * i
print("Factorial : ", factorial)    