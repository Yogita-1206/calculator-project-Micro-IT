print("Welcome to the simple mobile-style calculator")

while True:
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operation (+, -, *, /,=): ") 
        
        if operator == '=':
            result = num1
            print("Result:", result)
            break
        
        
        num2 = float(input("Enter second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Error! Division by zero.")
                continue
            result = num1 / num2
        else:
            print("Invalid operation! please Try again.")
            continue
        
        print("Result:", result)

    except ValueError:
        print("Invalid input! Please enter numerical values.")


