
programming_dictionary = {
    "Bug": "An error in a program",
    "Function": "A piece of code that you can call over and over",
}

print(programming_dictionary)

# Adding/Changing a dictionary element
programming_dictionary["Loop"] = "The action of doing something again and again"

# Print a dictionary
print(programming_dictionary)

# Access a dictionary element by its key
print(programming_dictionary["Bug"])

# Wipe a dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

