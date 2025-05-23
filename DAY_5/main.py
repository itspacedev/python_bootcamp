fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")

print("\n---------------------\n")

student_scores = [150, 12, 38, 12, 184, 90, 182, 171, 100]
total_exam_score = sum(student_scores)
print(f"Total exam score: {total_exam_score}")

total_score_sum = 0
for score in student_scores:
    total_score_sum += score

print(f"Total exam score using loop: {total_score_sum}")

max_score = max(student_scores)
print(f"Maximum score: {max_score}")

max_score_value = student_scores[0]
for score in student_scores:
    if score > max_score_value:
        max_score_value = score

print(f"Maximum score using loop: {max_score_value}")

print("\n---------------------\n")

for number in range(1, 10):
    print(number)

print("\n---------------------\n")

for number in range(1, 13, 3):
    print(number)

print("\n---------------------\n")

# Gaussian challenge
gaussian_sum = 0
for number in range(1, 100 + 1):
    gaussian_sum += number

print(f"Gaussian challenge - sum of all numbers from 1 to 100: {gaussian_sum}")
