numbers = []
input_number = -1
print()
print("Enter a list of numbers, , type 0 when finished.")
while input_number != 0:
    input_number = int(input("Enter number: "))
    numbers.append(input_number)

print(numbers)
total = 0
for number in numbers:
    total += number

print(f"The sum is: {total}")
average = total / len(numbers)
print(f"The average is: {average}")
# finding the largest number

largest = -100000
for number in numbers:
    if number > largest:
        largest = number
print(f"The largest number is: {largest}")

smallest = 1000000
for number in numbers:
    if number > 0 and smallest > number:
        smallest = number
print(f"The smallest positive number is: {smallest}")

numbers.sort()

print("The sorted list is:")
for number in numbers:
    print(f"{number}")