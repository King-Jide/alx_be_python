def perform_operation(num1, num2, operation):
    '''
    Performs basic arithmetic operation: add, subtract, multiply and divide.

    Args:
        num1(float): The first number. 
        num2(float): The Second number.
        operatiion(str): The operation to perform
    
    Returns:
        float or str: Result of the operation, or an error message.     
    '''


    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        return "Invalid Operation"
    
 
    
