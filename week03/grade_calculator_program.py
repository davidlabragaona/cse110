"""
Author: 8PM Group
Purpose: Write a program that determines the letter grade for a course according
to the following scale:

    A >= 90
    B >= 80
    C >= 70
    D >= 60
    F < 60

"""

# Let's ask the user to enter the grade percentage:
grade = input("Enter your grade percentage: ")
# store the number in numeric format
grade_numeric = int(grade)

# Grade Logic
if grade_numeric >= 90:
    letter = "A"
elif grade_numeric >= 80:
    letter = "B"
elif grade_numeric >= 70:
    letter = "C"
elif grade_numeric >= 60:
    letter = "D"
else:
    letter = "F"

# Sign Logic (Stretch Challenge #1)
# We use the reminder operator
# If the reminder is >= 7 then we assign a + sign
# If the reminder is < 3 then we assign a - sign
# otherwise, there is no sign
reminder = (grade_numeric % 10)
if reminder >= 7:
    sign = "+"
elif reminder >= 3:
    sign = ""
else:
    sign = "-"

# Stretch challenge #2
if letter == "A" and sign == "+":
    sign = ""

# Stretch challenge #3
if letter == "F":
    sign = ""


# Core Requirement #3
print(f"Your grade is: {letter}{sign}")

# Core Requirement #2
if grade_numeric >= 70:
    print("Congratulations. You have passed!")
else:
    print("Unfortunately you didn't pass. Please try again")
    
