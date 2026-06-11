print("--- Simple CLI Calculator ---")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Operations: + (Add), - (Subtract), * (Multiply), / (Divide)")
operation = input("Choose an operation: ")

if operation == "+":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Invalid operation selection.")
