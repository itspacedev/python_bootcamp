# def add(n1, n2):
#     return n1 + n2
#
#
# def subtract(n1, n2):
#     return n1 - n2
#
#
# def multiply(n1, n2):
#     return n1 * n2
#
#
# def divide(n1, n2):
#     return n1 / n2
#
#
# def calculate(calc_function, n1, n2):
#     return calc_function(n1, n2)


# print(calculate(add, 2, 4))


# Nested functions

# def outer_function():
#     print("I'm an outer function")
#
#     def nested_function():
#         print("I'm an inner function")
#
#     nested_function()
#
#
# outer_function()

# Return a function from another function

def outer_function():
    print("I'm an outer function")

    def nested_function():
        print("I'm an inner function")

    return nested_function


# outer_function()()
inner_function = outer_function()
inner_function()


