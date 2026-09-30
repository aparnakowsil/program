# A simple beginner-friendly calculator program

def main():
    try:
        # 1. Ask the user for the first number
        # We use float() to allow decimal numbers as well as integers
        first_number = float(input("Enter first number: "))

        # 2. Ask the user to select an operation
        operation = input("Enter operation (+, -, *, /, %): ")

        # 3. Ask the user for the second number
        second_number = float(input("Enter second number: "))

        # 4. Perform the calculation based on the chosen operation
        if operation == '+':
            result = first_number + second_number
        elif operation == '-':
            result = first_number - second_number
        elif operation == '*':
            result = first_number * second_number
        elif operation == '/':
            # Check for division by zero to prevent program crash
            if second_number == 0:
                print("\nError: Cannot divide by zero.")
                return
            result = first_number / second_number
        elif operation == '%':
            # Check for modulus by zero to prevent program crash
            if second_number == 0:
                print("\nError: Cannot perform modulus by zero.")
                return
            result = first_number % second_number
        else:
            # Handle any operation input that isn't in our list
            print("\nError: Invalid operation.")
            return

        # Format the result to look clean (e.g., 30 instead of 30.0)
        if result.is_integer():
            result = int(result)

        # Display the result with an empty line before it
        print(f"\nResult: {result}")

    except ValueError:
        # Handle cases where the user types letters or symbols instead of a number
        print("\nError: Invalid input. Please enter numbers.")

if __name__ == "__main__":
    main()
