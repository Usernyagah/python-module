# Get user inputs
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

# Validate the operation
if operation not in ['+', '-', '*', '/']:
    print("Invalid operation.")
    exit()

# Check division by zero
if operation == '/' and b == 0:
    print("Cannot divide by zero!")
    exit()

# Perform the calculation
if operation == '+':
    result = a + b
elif operation == '-':
    result = a - b
elif operation == '*':
    result = a * b
elif operation == '/':
    result = a / b

# Format numbers to display as integers if they are whole numbers
formatted_a = int(a) if a.is_integer() else a
formatted_b = int(b) if b.is_integer() else b
formatted_result = int(result) if result.is_integer() else result

# Display the result
print(f"{formatted_a} {operation} {formatted_b} = {formatted_result}")
