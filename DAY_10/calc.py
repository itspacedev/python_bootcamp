from art import logo


def add(a, b):
    """
    Returns the sum of two numbers
    """
    return a + b


def subtract(a, b):
    """
    Returns the result after subtracting b from a
    """
    return a - b


def multiply(a, b):
    """
    Return the result of multiplying a and b
    """
    return a * b


def divide(a, b):
    """
    Return the result of dividing a by b
    """
    return a / b


# Store operations in a dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Call add function using a dictionary
print(operations["+"](2, 9))

first_number = 0.0
second_number = 0.0
result_number = 0.0

new_calculation = True
stop = False
while not stop:
    print(logo)

    if new_calculation:
        first_number = float(input("What is the first number?: "))

    operation = input("Pick an operation (+, -, *, /): ")

    # if not new_calculation:
    second_number = float(input("What is the next number?: "))

    result_number = operations[operation](first_number, second_number)

    print(f"{first_number} {operation} {second_number} = {result_number}")

    step = input(f"Type 'y' to continue calculating with {result_number}, 'n' to start new calculation, or 'exit' to quit the calculator: ")
    if step == "exit":
        stop = True
    elif step == "y":
        first_number = result_number
        second_number = 0.0
        result_number = 0.0
        new_calculation = False
    else:
        first_number = 0.0
        second_number = 0.0
        result_number = 0.0
        new_calculation = True
