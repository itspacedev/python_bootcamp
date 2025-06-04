import random
import pandas

numbers = [1, 2, 3]

# Creating a new list of numbers where each number is increased by 1
new_list = []
for n in numbers:
    new_number = n + 1
    new_list.append(new_number)
print(new_list)

# Creating a new list of numbers using List comprehension
new_list_of_numbers = [one_number + 1 for one_number in numbers]

print(new_list_of_numbers)

name = "Alice"
name_letters = [letter for letter in name.lower()]
print(name_letters)

numbers_doubled = [2 * n for n in range(1, 5)]
print(numbers_doubled)


usernames = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_usernames = [username for username in usernames if len(username) <= 4]
print(short_usernames)

upper_long_names = [username.upper() for username in usernames if len(username) >= 5]
print(upper_long_names)

# Dictionary Comprehension
usernames = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students = {s_name: random.randint(40, 100) for s_name in usernames}
print(students)

passed_students = {student: score for (student, score) in students.items() if score > 70}
print(passed_students)

# Iterate over pandas dataset
student_dict = {
    "student": ["Alice", "Bob", "Tommy"],
    "score": [45, 82, 91],
}

df = pandas.DataFrame(student_dict)
print(df)

for (key, value) in df.items():
    print(value)

# Loop through each row of a pandas dataset
for (index, row) in df.iterrows():
    print(index)
    print(row)
    print(f"Student name at index {index}: {row['student']}")
