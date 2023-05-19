# Author: David Labra Gaona
# Purpose: Lists program
# Date: 2023-05-18

friends = []
friend_name = ""

while friend_name.lower() != "end":
    friend_name = input("Type the name of a friend: ")
    if friend_name.lower() != "end":
        friends.append(friend_name)

print()
print("Your friends are:")
for friend in friends:
    print(friend)


# Shopping list
item = ""
shopping_list = []
print("Please enter the items of the shopping list (type: quit to finish):")
while item.lower() != "quit":
    item = input("Item: ")
    if item.lower() != "quit":
        shopping_list.append(item)

print()
print("The shopping list is:")
for item in shopping_list:
    print(item)


print()
print("The shopping list with indexes is:")
for i, item in enumerate(shopping_list):
    print(f"{i}. {item}")

print()
i = int(input("Which item would you like to change? "))
item = input("What is the new item? ")

shopping_list[i] = item

print()
print("The shopping list with indexes is:")
for i, item in enumerate(shopping_list):
    print(f"{i}. {item}")

