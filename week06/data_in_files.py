#Author: David Labra Gaona
#Purpose: Work with data in files


people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

name = ""
age = 0
youngest_name = ""
youngest_age = 999

for line in people:
    person = line.split()
    name = person[0]
    age = int(person[1])

    print(f"Name: {name}, Age: {age}")

    #youngest
    if age < youngest_age:
        youngest_age = age
        youngest_name = name

print(f"The youngest person is: {youngest_name}")
