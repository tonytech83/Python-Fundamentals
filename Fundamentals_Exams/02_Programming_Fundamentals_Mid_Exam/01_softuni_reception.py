first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
students_count = int(input())

sum_students_per_hour = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency
hours = 0

while True:

    if students_count <= 0:
        break

    students_count -= sum_students_per_hour
    hours += 1

    if hours % 4 == 0:
        hours += 1

print(f'Time needed: {hours}h.')
