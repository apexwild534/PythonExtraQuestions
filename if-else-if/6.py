def calculate_income_tax(income):
    if income <= 0:
        tax = 0
    elif income <= 10000:
        tax = income * 0.10
    elif income <= 50000:
        tax = 10000 * 0.10 + (income - 10000) * 0.20
    elif income <= 100000:
        tax = 10000 * 0.10 + 40000 * 0.20 + (income - 50000) * 0.30
    else:
        tax = 10000 * 0.10 + 40000 * 0.20 + 50000 * 0.30 + (income - 100000) * 0.40

    return tax

# Input the income from the user
income = float(input("Enter your annual income: "))

# Calculate and print the income tax
income_tax = calculate_income_tax(income)
print(f"Your income tax is: {income_tax:.2f}")
