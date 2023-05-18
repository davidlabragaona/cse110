# Author: David Labra Gaona
# Purpose: Wordle game

secret = "helaman"
word_len = len(secret)
win = False
tries = 0

print("Welcome to the word guessing game!\n")
print("Your hint is: ", end = "")

for i in range(word_len):
    print("_ ", end = "")
print()


in_word = False
# Game logic
while not win:
    guess = input("What is your guess? ")

    if len(guess) != word_len:
        print("Sorry, the guess must have the same number of letters as the secret word.")
    else:
        if guess.lower() == secret.lower():
            print("Congratulations! You guessed it!")
            print(f"It took you {tries + 1} guesses")
            win = True
        else:
            print("Your hint is: ", end="")
            # we check for the same spot same letter
            for i in range(word_len):
                if guess[i].lower() == secret[i].lower():
                    print(guess[i].upper() + " ", end = "")
                else:
                    for j in range(word_len):
                        if guess[i].lower() == secret[j].lower():
                            in_word = True
                            j = word_len
                    if in_word:
                        print(guess[i] + " ", end="")
                    else:
                        print("_ ", end="")
                    in_word = False
    tries = tries + 1
    print()

