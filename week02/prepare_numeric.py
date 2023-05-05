""""
Author: David Labra Gaona

"""


#Write a program that does the following:

    # 1. Prompt the user for their age. Convert it to a number, add one to it, and tell them how old they will be on their next birthday.

    # 2. Prompt the user for the number of egg cartons they have. Assume each carton holds 12 eggs, multiply their number by 12, and display the total number of eggs.

    # 3. Prompt the user for a number of cookies and a number of people. Then, divide the number of cookies by the number of people to determine how many cookies each person gets.

age = input('How old are you?')
print('On your next birthday, you will be ' + str(int(age) + 1) + '\n')

eggs = input('How many egg cartons do you have?')
print('You have ' + str(int(eggs) * 3) + ' eggs \n')

cookies = input('How many cookies do you have?')
people = input('How many people are there?')
print(f'Each person may have {float(cookies) / float(people)} \n')
