
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is undefined."
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error: Square root of a negative number is undefined."
    return math.sqrt(x)

def modulo(x, y):
    return x % y

def factorial(x):
    if x < 0:
        return "Error: Factorial of a negative number is undefined."
    return math.factorial(x)

def calculator():
    print("Welcome to the CLI Calculator!")
    print("Available operations: add, subtract, multiply, divide, power, sqrt, modulo, factorial")
    print("Type 'exit' to quit the calculator.")
    
    while True:
        operation = input("Enter operation: ").strip().lower()
        if operation == "exit":
            print("Good Bye!!")
            break

        if operation in ["add", "subtract", "multiply", "divide", "power", "modulo"]:
            try:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue
            if operation == "add":
                print(f"Result: {add(x, y)}")
            elif operation == "subtract":
                print(f"Result: {subtract(x, y)}")
            elif operation == "multiply":
                print(f"Result: {multiply(x, y)}")
            elif operation == "divide":
                print(f"Result: {divide(x, y)}")
            elif operation == "power":
                print(f"Result: {power(x, y)}")
            elif operation == "modulo":
                print(f"Result: {modulo(x, y)}")

        elif operation == "sqrt":
            try:
                x = float(input("Enter the number: "))
                print(f"Result: {square_root(x)}")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        
        elif operation == "factorial":
            try:
                x = int(input("Enter an integer: "))
                print(f"Result: {factorial(x)}")
            except ValueError:
                print("Invalid input. Please enter an integer.")

        else:
            print("Invalid operation. Try again.")

if __name__ == "__main__":
    calculator()
