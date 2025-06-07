# KeyError
# my_dict = {"name": "Alice"}
# print(my_dict["age"])

# IndexError
# fruits_list = ["Apple", "Banana", "Cherry"]
# print(fruits_list[5])

# TypeError
# text = "abc"
# print(text + 5)

# ZeroDivisionError
# a = 5
# b = 0
# c = a / b

# FileNotFoundError
# try:
#     print("[1] - Debug comment")
#     file = open("a_file.txt")
#     print("[2] - Debug comment")
#     my_dict = {"key": "value"}
#     print(my_dict["another_key"])
# except FileNotFoundError as error_message:
#     print("[3] - Debug comment")
#     print(error_message)
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print("[4] - Debug comment")
#     print(error_message)
#     print(f"The key {error_message} does not exist")
# else:
#     print("[5] - Debug comment")
#     content = file.read()
#     print(content)
# finally:
#     print("[6] - Debug comment")
#     file.close()
#     raise TypeError("This is my fantastic error :)")

# Calculate Body Mass Index
# ValueError
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / (height ** 2)
print(bmi)
