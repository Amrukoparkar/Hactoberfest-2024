import math

# Function to perform basic arithmetic operations
def arithmetic_operations():
    print("\n--- Basic Arithmetic Operations ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
    else:
        print("Invalid choice.")

# Function to perform trigonometric operations
def trigonometric_operations():
    print("\n--- Trigonometric Operations ---")
    print("1. Sine")
    print("2. Cosine")
    print("3. Tangent")

    choice = input("Enter choice (1/2/3): ")

    angle = float(input("Enter the angle in degrees: "))
    radians = math.radians(angle)

    if choice == '1':
        print(f"Result: sin({angle}) = {math.sin(radians)}")
    elif choice == '2':
        print(f"Result: cos({angle}) = {math.cos(radians)}")
    elif choice == '3':
        print(f"Result: tan({angle}) = {math.tan(radians)}")
    else:
        print("Invalid choice.")

# Function to perform logarithmic operations
def logarithmic_operations():
    print("\n--- Logarithmic Operations ---")
    print("1. Natural Logarithm (ln)")
    print("2. Logarithm base 10 (log10)")

    choice = input("Enter choice (1/2): ")

    num = float(input("Enter a positive number: "))

    if num <= 0:
        print("Error: Logarithm of non-positive numbers is not defined.")
    else:
        if choice == '1':
            print(f"Result: ln({num}) = {math.log(num)}")
        elif choice == '2':
            print(f"Result: log10({num}) = {math.log10(num)}")
        else:
            print("Invalid choice.")

# Function to perform power and root operations
def power_root_operations():
    print("\n--- Power and Root Operations ---")
    print("1. Square")
    print("2. Cube")
    print("3. Power")
    print("4. Square Root")
    print("5. Cube Root")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice in ['1', '2', '3', '4', '5']:
        num = float(input("Enter a number: "))

        if choice == '1':
            print(f"Result: {num}^2 = {num ** 2}")
        elif choice == '2':
            print(f"Result: {num}^3 = {num ** 3}")
        elif choice == '3':
            power = float(input("Enter the power: "))
            print(f"Result: {num}^{power} = {num ** power}")
        elif choice == '4':
            if num < 0:
                print("Error: Square root of a negative number is not real.")
            else:
                print(f"Result: √{num} = {math.sqrt(num)}")
        elif choice == '5':
            print(f"Result: ∛{num} = {num ** (1/3)}")
    else:
        print("Invalid choice.")

# Main calculator function
def calculator():
    while True:
        print("\n--- Complex Calculator ---")
        print("1. Arithmetic Operations")
        print("2. Trigonometric Operations")
        print("3. Logarithmic Operations")
        print("4. Power and Root Operations")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '1':
            arithmetic_operations()
        elif choice == '2':
            trigonometric_operations()
        elif choice == '3':
            logarithmic_operations()
        elif choice == '4':
            power_root_operations()
        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the calculator
calculator()
