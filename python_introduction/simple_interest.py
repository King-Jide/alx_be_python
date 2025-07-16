# This program calculates simple interest
principal = 1000
time = 3
rate = float(0.05)
def calculate_simple_interest(principal, time, rate):
    """
    Calculate simple interest.

    Parameters:
    principal (float): The principal amount.
    time (float): The time in years.
    rate (float): The rate of interest per year.

    Returns:
    float: The calculated simple interest.
    """
    return principal * time * rate  

interest = calculate_simple_interest(principal, time, rate)
print("The simple interest is:", interest)