print(len("Hello"))

# Subscripting
print("Hello!"[5])

# The last character in the string
print("Hello~"[-1])

# Concatenating strings
print("123" + "345")

# Integer = Whole number
print(123 + 456)

# Large integers formatting
print(1234567)

print(1_234_567)

# Float = Floating point number
print(3.14159)

# Large float number formatting
print(1_234_567.890)

# Boolean (True/False)
print(True)
print(False)

# Check the data type of a string
print(type("Hello"))

# Check the data type of an integer
print(type(1_234_567))

# Check the data type of a float number
print(type(3.14159))

# Check the data type of a boolean
print(type(True))

# Conversion between data types
print("\n----- Conversion -----\n")

# Convert a string to an integer
print(type(int("123")))
print(int("123") + int("456"))

print(type(float("3.24")))
print(float("1.11") + float("2.22"))

print(type(bool("False")))

# Converting the length of a string to a string in order to print it using concatenation
# print("Number of letters in your name: " + str(len(input("What is your name?"))))

# Conversion between data types
print("\n----- Mathematical Operations -----\n")

print(123 + 456)
print(7 - 3)
print(3 * 2)

print(6 / 3)
print(type(6 / 2))

print(9 // 3)
print(type(9 // 3))

print(4 ** 2)

print(3 + 3 - 3 + 3 - 3)

# Calculate Body Mass Index
print("\n----- Calculate Body Mass Index -----\n")

weight = 84
height = 1.65
bmi = weight / (height ** 2)
print(bmi)
print(int(bmi))
print(round(bmi))
print(round(bmi, 2))

# f Strings
print("\n----- f Strings -----\n")
score = 0
height = 1.8
is_winning = True

print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}")

