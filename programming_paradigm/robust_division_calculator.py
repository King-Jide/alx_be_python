
def safe_divide(numerator, denominator):
    """
    Safely divides two numbers and prints the result.

    Parameters:
        numerator: The number to be divided (can be int, float, or str convertible to float).
        denominator: The number by which to divide (can be int, float, or str convertible to float).

    Behavior:
        Prints the result rounded to two decimal places.
        Handles division by zero and non-numeric input errors gracefully.
    """
    try:
        num = float(numerator)
        denom = float(denominator)
        result = num / denom
        return f"The result of the division is {result:.2f}"
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except ValueError:
        print("Error: Please enter numeric values only.")
        return None 
    

