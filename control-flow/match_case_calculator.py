#Prompt user for input - recive input for two numbers (num1 & num2)
while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
    #Ask for the type of operation they’d like to perform: Choose the operation (+, -, *, /):
        operation = input ("Choose the operation (+, -, *, /): ").strip()

        # result = (
        #     "multiply" if  operation == '*'
        #     else "addition" if operation == "+"
        #     else "subtraction" if operation == "-"
        #     else "division" if operation == "/"
        #     else ""
        # )

        # match result:
        #     case "multiply":
        #         print(num1 * num2)
        #     case "addition":
        #         print(num1 + num2)
        #     case "subtraction":
        #         print(num1-num2)
        #     case "division":
        #         if num2 == 0:
        #             print("Cannot divide by Zero")
        #         else:
        #             print(num1/num2)
        #improved use of match case
        match operation:
            case '+':
                print(f"The result is {num1 + num2}")
            case '-':
                print(f"The result is {num1 - num2}")
            case '*':
                print(f"The result is {num1 * num2}")
            case '/':
                if num2 == 0:
                    print("Cannot divide by zero.")
                else:
                    print(f"The result is {num1 /num2}")
    except ValueError:
        print("Invalid Input, please enter numbers only.")
    
       # Ask to perform another calculation
    play_again = input("Do you want to calculate again? (y/n): ").strip().lower()
    if play_again != 'y':
        print("Thanks for using the calculator. Goodbye! 👋")
        break




    