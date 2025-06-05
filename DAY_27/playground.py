# Unlimited positional arguments
def add(*args):
    print(type(args))
    print(args[0])
    total = 0
    for number in args:
        total += number
    return total


print(add(1, 2, 3))
print(add(1, 2, 3, 4, 5, 6))


# Unlimited keyword arguments
def calculate(n, **kwargs):
    print(type(kwargs))
    print(kwargs)

    for (key, value) in kwargs.items():
        print(f"kwargs[{key}] = {value}")

    n += kwargs["add"]
    n *= kwargs["multiply"]

    return n


print(calculate(2, add=1, multiply=4))


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
