# Write a Python program to calculate the area of a circle given its radius using the formula
# area=π×r^2 ( Take pie as 3.14)
#
# Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.
#
# Use the ternary operator to find the maximum of three numbers entered by the user.
# Develop a Python script that calculates the square and cube of a given number.

#Task 1
r=int(input("Enter a value for raduis,r\n"))
A=3.14*(r**2)
print("Area of you circle is",A)

#Task 2
num1=int(input("Enter a number\n"))
num2=int(input("Enter a number\n"))
if num1==num2:print("Both numbers are same!")
elif num1>num2:print("Num1 greater than num2")
else: print("Num1 is less than num2")

#Task3
n1=int(input("Enter first number:\n"))
n2=int(input("Enter second number:\n"))
n3=int(input("Enter third number:\n"))
if n1>n2 and n1>n3:print("n1 is greatest")
elif n2>n1 and n2>n3:print("n2 is greatest")
else:print("n3 is greatest")

#Task4
num=int(input("Enter a number\n"))
square=num**2
cube=num**3
print(f"Square of {num} is",square)
print(f"Cube of {num} is",cube)
