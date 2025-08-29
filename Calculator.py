def calculator():
    try:
        # Get input from user
        num1 = float(input("Enter first number: "))
        num27 = float(input("Enter second number: "))
        num3 = float(input("Just Stop: "))
        operation = input("Enter operation (+, -, *, /): ")

        # Perform calculation based on operation
        if operation == '+':
            result = num1 + num27
            print(f"{num1} + {num27} = {result}")
            print("You Should have stopped when i told you to")
        elif operation == '-':
            result = num1 - num27
            print(f"{num1} - {num27} = {result}")
            print("You Should have stopped when i told you to")
        elif operation == '*':
            result = num1 * num27
            print(f"{num1} * {num27} = {result}")
            print("You Should have stopped when i told you to")
        elif operation == '/':
            if num27 == 0:
                print("Error: Cannot divide by zero!")
            else:
                result = num1 / num27
                print(f"{num1} / {num2} = {result}")
                print("You Should have stopped when i told you to")

        else:
            print("Error: Invalid operation! Please use +, -, *, or /")
            
    except ValueError:
        print("Error: Please enter valid numbers!")

# Run the calculator
if __name__ == "__main__":
    calculator()