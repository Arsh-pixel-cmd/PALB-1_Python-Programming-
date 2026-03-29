def arithmetic_ops(a, b):
    print(f"Addition: {a + b}")
    print(f"Subtraction: {a - b}")
    print(f"Multiplication: {a * b}")
    try:
        print(f"Division: {a / b}")
        print(f"Modulus: {a % b}")
    except ZeroDivisionError:
        print("Cannot divide by zero")

if __name__ == "__main__":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    arithmetic_ops(a, b)
