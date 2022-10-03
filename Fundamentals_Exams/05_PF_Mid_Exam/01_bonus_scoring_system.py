import math

number_of_students = int(input())
lectures_number = int(input())
additional_bonus = int(input())

max_bonus = 0
max_lectures = 0

for student in range(number_of_students):
    student_attendances = int(input())
    current_bonus = student_attendances / lectures_number * (5 + additional_bonus)
    if current_bonus > max_bonus:
        max_bonus = current_bonus
        max_lectures = student_attendances

print(f'Max Bonus: {math.ceil(max_bonus)}.\nThe student has attended {max_lectures} lectures.')
