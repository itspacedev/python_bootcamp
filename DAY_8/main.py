def greet():
    print("Thing 1")
    print("Thing 2")
    print("Thing 3")


# greet()


# Function that allow for inputs
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}")


# greet_with_name("Vinny")


# Function with more than one input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


greet_with("Vinny", "London")

# Call a function using keyword arguments
greet_with(location="Ibiza", name="Tony")

