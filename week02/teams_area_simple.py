"""
Author: David Labra Gaona
Date: 28 APR 2023
Time: 06:10

Purpose: Write a program to compute the areas of three different shapes.
Prompt for the necessary information, then compute and display the area, as
follows:

Make sure that your program can appropriately handle decimal values as well as
whole numbers.
"""

import math

# Core requirement + stretch challenge #3

# square = float(input("What is the length in centimiters of a side of the square? "))
# square2 = square ** 2
# print("The area of the square is: {:.1f} cm^2 and {} m^2".format(square2, square2 / 10000))
# print()
# 
# rect_lenght = float(input('What is the length in centimiters of the rectangle? '))
# rect_width = float(input('What is the width in centimiters of the rectangle? '))
# area = rect_lenght * rect_width
# print(f"The area of a rectangle is: {(area):.1f} cm^2 and {(area / 10000)} m^2")
# print()
# 
# circle_radius = float(input("What is the radius in centimiters of the circle? "))
# area = circle_radius ** 2 * math.pi
# print("The area of the circle is: {:.1f} cm^2 and {} m^2".format(area, area / 10000))
# print()

# Stretch Challenge #2
length_cm = float(input('Enter a lenght in centimiters: '))
print()
print("The area of a square of length {} cm is {} cm^2".format(length_cm, length_cm ** 2))
print("The volume of the cube of length {} cm is: {} cm^3".format(length_cm, length_cm ** 3))
print()

radius_cm = length_cm
print()
print("The area of a circle of radius {} cm is {} cm^2".format(length_cm, math.pi * radius_cm ** 2))
print("The volume of the sphere of radius {} cm is: {} cm^3".format(length_cm, (4 / 3) * math.pi * radius_cm ** 3))
print()

