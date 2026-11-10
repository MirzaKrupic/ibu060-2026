def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


a = int(input("First: "))
op = input("Operator: ")
b = int(input("Second: "))
if op == "/" and b == 0:
    print("Cannot divide by zero")
elif op == "+":
    print(add(a, b))
elif op == "-":
    print(subtract(a, b))
elif op == "*":
    print(multiply(a, b))
elif op == "/":
    print(divide(a, b))
else:
    print("Unknown operator")
