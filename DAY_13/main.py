import random


def my_function():
    for i in range(1, 20):  # change the range to range(1, 21) so it reaches 20
        # print(i)
        if i == 20:
            print("You got it!")


my_function()


# Reproduce a bug: IndexError: list index out of range
# dice_images = ["1", "2", "3", "4", "5", "6"]
# dice_num = random.randint(1, 6)
# print(dice_images[dice_num])
dice_images = ["1", "2", "3", "4", "5", "6"]
print(f"Length of a list: {len(dice_images)}")
dice_num = random.randint(0, 5)  # change min and max values between which the random number is generated (inclusively)
print(f"Random index generated: {dice_num}")
print(dice_images[dice_num])


# Try except block
try:
    age = int(input("How old are you?: "))
except ValueError:
    print("You have typed in an invalid number. Please try again with a numerical response such as 15.")

if age > 18:
    print(f"You can drive at age {age}")
