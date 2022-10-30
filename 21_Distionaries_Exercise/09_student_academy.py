pair_rows = int(input())

students_grades = {}

for _ in range(pair_rows):
    name = input()
    grade = float(input())

    if name not in students_grades:
        students_grades[name] = []
        students_grades[name].append(grade)
    else:
        students_grades[name].append(grade)

for name, grades in students_grades.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.5:
        print(f'{name} -> {average_grade:.2f}')
