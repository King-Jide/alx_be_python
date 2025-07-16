#personal finance calculator
#User to input their monthly income and expenses
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))
#Calculate the monthly savings
monthly_savings = monthly_income - monthly_expenses
#Calculate Projected Annual Savings
projected_annual_savings = (monthly_savings * 12) + (monthly_savings *12 * 0.05)  # Assuming a 5% increase in savings each year
#Output the results
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings}.")