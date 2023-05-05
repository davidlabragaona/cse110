# Creativity: Added drinks price, drinks count and discount rate

"""
Author: David Labra Gaona
Date: 28 ABR 2023
Time: 14:40
Purpose: Compute the price of a meal as follows by asking for the price of 
child and adult meals, the number of each, and then the sales tax rate. Use 
these values to determine the total price of the meal. Then, ask for the payment
amount and compute the amount of change to give back to the customer.

Keep in mind that some of these values are floating point numbers (they can have
decimals) and some of them are integers (whole numbers).
"""

# Let's store the values
child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of a adult's meal? "))
drinks_price = float(input("What is the price for drinks? "))
children_count = int(input("How many children are there? "))
adult_count = int(input("How many children are there? "))
drinks = int("How many drinks? ")
tax_rate = float(input("What is the sales tax rate? "))
promotion_rate = float(input("Discount rate"))

# Calculations
subtotal = (child_meal * children_count) + (adult_meal * adult_count)
promotion = subtotal * promotion_rate / 100
tax = subtotal * tax_rate / 100
total = subtotal + tax - promotion

# Let's display the information
print()
print("***********************************************")
print("Subtotal: $ {:.2f}".format(subtotal))
print("Sales Tax: $ {:.2f}".format(tax))
print("Total: $ {:.2f}".format(total))

# Payment and Change
print("***********************************************")
payment = float(input("What is the payment amount? "))
print("Change: ${:.2f}".format(payment - total))
