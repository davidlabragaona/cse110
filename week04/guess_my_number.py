"""
Author: Group 8PM
Purpose: Write a Guess my Number game in python
"""

import random

#magic_number = int(input("What is the magic number? "))

response = "yes"

#stretch challenge #2
while response.lower() == "yes":

   magic_number = random.randint(1, 100)

   #stretch challenge #1
   track_guesses = 0

   #for testing purposes, let's print the value
   #print(magic_number)
   guess_number = 0

   while guess_number != magic_number:
       guess_number = int(input("What is your guess? "))
       track_guesses = track_guesses + 1
   
       if guess_number > magic_number:
           print("Lower")
       elif guess_number < magic_number:
           print("Higher")

   print(f"You guessed it! Number of tries: {track_guesses}")

   response = input("Would you like to play again? (Yes/No)")
