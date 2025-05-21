print("Welcome to the Tip Calculator!")

total_bill = float(input("What was the total bill?\n"))
tip_percentage = int(input("How much tip (%) would you like to give? 10, 12, or 15?\n"))
number_of_people = int(input("How many people to split the bill?\n"))

# Calculate the total bill including the tip percentage
total_bill *= 1 + (tip_percentage / 100)

# Calculate each person bill
each_person_bill = round(total_bill / number_of_people, 2)

print(f"Each person should pay: ${each_person_bill}")