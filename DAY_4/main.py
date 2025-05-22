import random
import my_module

print(f"My favourite number from module: {my_module.my_favourite_number}\n")

random_integer = random.randint(3, 12)
print(f"Random integer number is: {random_integer}")

random_float_0_to_1 = random.random()
print(f"Random float number from 0 to 1 is: {random_float_0_to_1}")

random_uniform = random.uniform(3.2, 4.9)
print(f"Random uniform float number is: {random_uniform}")
