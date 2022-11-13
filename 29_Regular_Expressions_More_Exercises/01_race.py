import re

participants = input().split(', ')

pattern_letters = r'[A-Za-z]+'
pattern_digits = r'\d'
race = {}

while True:
    line = input()
    if line == 'end of race':
        break

    matched_letters = re.findall(pattern_letters, line)
    matched_digits = re.findall(pattern_digits, line)

    participant_name = ''
    participant_score = 0

    for letter in matched_letters:
        participant_name += letter

    for digit in matched_digits:
        participant_score += int(digit)

    if participant_name in participants:
        if participant_name in race.keys():
            race[participant_name] += participant_score
        else:
            race[participant_name] = participant_score

places = ['1st', '2nd', '3rd']
names = []
sorted_by_points = sorted(race.items(), key=lambda x: -x[1])
for kvp in list(sorted_by_points)[0:3]:
    names.append(kvp[0])

for idx in range(len(places)):
    print(f'{places[idx]} place: {names[idx]}')
