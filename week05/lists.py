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


