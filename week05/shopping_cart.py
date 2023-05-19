# Author: David Labra Gaona
# Purpose: Shopping Cart Assignement

# We define the menu options in a list
options = ["Add item", "View cart", "Remove item", "Compute total", "Quit"]

print("Welcome to the Shopping Cart Program!")

# working variables
# Initializing variables
option = 0
item = ""
shopping_list = []

while option != 5:
    print("\nPlease select one of the following: ")
    for i, item in enumerate(options):
        print(f"{i + 1}. {item}")

    option = int(input("\nPlease, enter an action: "))
    # Add item
    if option == 1:
        item = input("What item would you like to add? ")
        shopping_list.append(item)
        print(f"'{item}' has been added to the cart.")
    # View cart
    elif option == 2:
        print("The contents of the shopping cart are: ")
        for item in shopping_list:
            print(item)
    # quit
    elif option == 5:
        print("Thank you. Goodbye.")

