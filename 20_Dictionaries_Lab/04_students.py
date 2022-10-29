courses = {}

while True:
    data = input()
    if ':' not in data:
        break
    name, student_id, course = data.split(':')
    if course not in courses:
        courses[course] = {}
    courses[course][student_id] = name

if '_' in data:
    searched_course = data.replace('_', ' ')
else:
    searched_course = data

for course_name in courses:
    if course_name == searched_course:
        for key, value in courses[course_name].items():
            print(f'{value} - {key}')
