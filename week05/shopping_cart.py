#Creativity: validation of numeric option and price values

# Author: David Labra Gaona
# Purpose: Shopping Cart Assignement

# We define the menu options in a list
options = ["Add item", "View cart", "Remove item", "Compute total", "Quit"]

print("Welcome to the Shopping Cart Program!")

# working variables
# Initializing variables
option = 0
item = ""
price = 0.00
shopping_list = []
price_list = []
total = 0.00

while option != 5:
    print("\nPlease select one of the following: ")
    for i, item in enumerate(options):
        print(f"{i + 1}. {item}")

    option = input("\nPlease, enter an action: ")
    if option.isnumeric():
        option = int(option)
    else:
        print("Invalid option")
        continue
    # Add item
    if option == 1:
        item = input("What item would you like to add? ")
        price = input(f"What is the price of {item}? ")
        if price.isnumeric():
            price = float(price)
            shopping_list.append(item)
            price_list.append(price)
            print(f"'{item}' has been added to the cart.")
        else:
            print("Invalid price.")
    # View cart
    elif option == 2:
        print("The contents of the shopping cart are: ")
        for i, item in enumerate(shopping_list):
            print(f"\t{i+1}. {item} - ${price_list[i]:.2f}")
    elif option == 3:
        i = input("Which item would you like to remove? ")
        if i.isnumeric:
            i = int(i)
        else:
            print("Invalid option")
            continue
        if (i - 1) > len(shopping_list) or len(shopping_list) == 0:
            print("Sorry that is not a valid item number.")
        else:
            shopping_list.pop(i - 1)
            price_list.pop(i - 1)
            print("Item removed")
    elif option == 4:
        total = 0
        for p in price_list:
            total += p
        print(f"The total price of the items in the shopping cart is ${total:0.2f}")
    # quit
    elif option == 5:
        print("Thank you. Goodbye.")