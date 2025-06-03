# Read the file
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# print("\n-----------\n")

# Read the file
# with open("my_file.txt") as file_2:
#     contents = file_2.read()
#     print(contents)

# File open modes
# r - read
# w - write (removes existing content). If a file does not exist, it will be created
# a - append (does not remove existing content)

# Write to the file
with open("my_file.txt", mode="a") as file_3:
    file_3.write("\nHere is new text.")
