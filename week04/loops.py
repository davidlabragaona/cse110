"""
Author: David Labra Gaona
Purpose: Loops
"""

number = int(input("Please type a positive number: "))
while number <= 0:
    print("Sorry, that is a negative number. Please try again.")
    number = int(input("Please type a positive number: "))
print(f"The number is {number}.\n")

answer = "no"

while answer != "yes":
    answer = input("May I have a piece of candy? ").lower()
print("Thank you")

print("----------------------")

colors = ["red", "blue", "green", "yellow"]
for color in colors:
    print(color)

print("----------------------")

for number in range(0, 8):
    print(number + 1)

print("----------------------")

for number in range(0, 20, 2):
    print(number + 2)

print("----------------------")

word = "Commitment"
for letter in word:
    if letter == 'm':
        print("M")
    else:
        print(letter)

print("----------------------")

fav_letter = input("What is your favorite letter? ")
for letter in word:
    if letter == fav_letter:
        print(letter.upper(), end="")
    else:
        print(letter, end="")

print()
print("----------------------")

fav_letter = input("What is your favorite letter? ")
for letter in word:
    if letter == fav_letter:
        print("_", end="")
    else:
        print(letter, end="")

