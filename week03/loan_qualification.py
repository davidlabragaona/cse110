"""
Author: David Labra Gaona
Purpose: Qualifying for a loan
"""

loan_lenght = int(input("How large is your loan? (1-10): "))
credit_history = int(input("How good is your credit history? (1-10): "))
income = int(input("How high is your income? (1-10): "))
payment = int(input("How large is your down payment? (1-10): "))
is_approved = False

if loan_lenght >= 5:
    if credit_history >= 7 and income >= 7:
        is_approved = True
    elif credit_history >=7 or income >= 7:
        if payment >= 5:
            is_approved = True
        else:
            is_approved = False
    else:
        is_approved = False
else:
    if credit_history < 4:
        is_approved = False
    elif income >= 7 or payment >= 7:
        is_approved = True
    elif income >= 4 or payment >= 4:
        is_approved = True
    else:
        is_approved = False

if is_approved:
    print("The Loan was approved.")
else:
    print("The Loan was not approved.")