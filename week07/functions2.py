#Author: David Labra Gaona
#Purpose: Practice functions 2

import math

def compute_area_square(value):
    return value ** 2

def compute_area_rectangle(value1, value2):
    return value1 * value2

def compute_area_circle(radius):
    return math.pi * radius ** 2

value = float(input("Enter a value: "))
value = compute_area_circle(value)
print(f"The area of a circle is {value:.2f}")

response = ""
done = False

while not done:
  response = input("What kind of shape do you have? ").lower()
  if response == 'square':
      value = float(input("Enter the length of the side: "))
      value = compute_area_rectangle(value, value)
  elif response == 'rectangle':
      value = float(input("Enter the length of the side 1: "))
      value2 = float(input("Enter the length of the side 2: "))
      value = compute_area_rectangle(value, value2)
  elif response == 'circle':
      value = float(input("Enter the radius of the circle: "))
      value = compute_area_circle(value)
  elif response == 'quit':
      done = True
      continue
  else:
      print("Incorrect option, try again.")

  print(f"The area is {value:.2f}")
    