students = {}

while True:
    command = input()
    if ':' not in command:
        break
    name, student_id, course = command.split(':')
    students[student_id] = name, course

course_name = ''

if '_' in command:
    course_name = command.replace('_', ' ')
else:
    course_name = command

for key, value in students.items():
    if course_name in value:
        print(f'{value[0]} - {key}')
