# Calculate income tax for the given income by adhering to the rules

# Pseudocode

# if it is adhere to $10000
def income_tax(income):
    if income <= 10000:
        tax = 0
# if it is adhere to $20000
    elif income <= 20000:
        tax = (income - 10000) * 0.10
# else and return
    else:
        tax = 10000 * 0 + 10000 * 0.10 + (income - 20000) * 0.20
    
    return tax
# user input code
user_income = float(input("provide your income: "))
income_tax = income_tax(user_income)
# print the results
print(f"Income Tax: ${income_tax}")