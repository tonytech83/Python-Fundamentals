def submissions_per_lang(submissions, language):
    if language not in submissions:
        submissions[language] = 1
    else:
        submissions[language] += 1


def ban_student(programming_languages, student_name):
    for language, student_names in programming_languages.items():
        if student_name in student_names.keys():
            programming_languages[language].pop(student_name)


def init_student(programming_languages, student_name, language, points):
    if language not in programming_languages:
        programming_languages[language] = {}
        programming_languages[language][student_name] = points
    else:
        if student_name not in programming_languages[language].keys():
            programming_languages[language][student_name] = points
        else:
            if programming_languages[language][student_name] < points:
                programming_languages[language][student_name] = points


programming_languages = {}
submissions = {}

while True:
    line = input()
    if line == 'exam finished':
        break

    data = line.split('-')
    if len(data) > 2:
        student_name = data[0]
        language = data[1]
        points = int(data[2])
        submissions_per_lang(submissions, language)
        init_student(programming_languages, student_name, language, points)
    else:
        student_name = data[0]
        ban_student(programming_languages, student_name)

print('Results:')
for lang in programming_languages:
    for user, points in programming_languages[lang].items():
        print(f'{user} | {points}')
print('Submissions:')
for land, subs in submissions.items():
    print(f'{land} - {subs}')
