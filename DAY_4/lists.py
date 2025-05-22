states_of_america = ["Delaware", "Pennsylvania"]

print(f"First state in the list is: {states_of_america[0]}")

states_of_america[1] = "Pencilvenia (new name)"

print(f"Second state in the list is: {states_of_america[1]}")

states_of_america.append("New State name")
print(f"New list after appending a new state is: {states_of_america}")

states_of_america.extend(['New State 2 (extended)', 'New State 3 (extended)'])
print(f"New extended list is: {states_of_america}")