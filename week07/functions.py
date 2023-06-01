#Author: David Labra Gaona
#Purpose: Practice functions

#function to display regular text
def display_regular(text):
    print(text)

#function to print uppercase text
def display_uppercase(text):
    print(text.upper())

#function to print lowercase text
def display_lowercase(text):
    print(text.lower())

text = input("What is your message to the world? ")
display_regular(text)
display_uppercase(text)
display_lowercase(text)
