"""
Author: David Labra Gaona
Purpose: Compare 2 numbers
"""

int1 = int(input("Enter the first integer: "))
int2 = int(input("Enter the second integer: "))

if int1 > int2:
    print("The first number is greater")
else:
    print("The first number is not greater")

if int1 == int2:
    print("The numbers are equal")
else:
    print("The numbers are not equal")

if int2 > int1:
    print("The second number is greater")
else:
    print("The second number is not greater")

animal = input("Please, enter your favorite animal: ")
if animal.lower() == 'horse':
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")
