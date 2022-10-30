courses = {}

while True:
    data = input()
    if data == 'end':
        break

    course, student_name = data.split(' : ')
    if course not in courses:
        courses[course] = []
        courses[course].append(student_name)
    else:
        courses[course].append(student_name)

for key, value in courses.items():
    print(f'{key}: {len(value)}')
    for name in value:
        print(f'-- {name}')
