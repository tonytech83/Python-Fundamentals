import re


def find_all_letters(current_line):
    """
    This function parse all letters from string according to a given pattern.
    Concatenate all parsed letters in name variable
    :param current_line: str
    :return: str
    """
    name = ''
    pattern = r'[A-Za-z]+'
    matched_letters = re.findall(pattern, current_line)
    for letter in matched_letters:
        name += letter
    return name


def find_all_digits(current_line):
    """
    This function parse all digits from string according to a given pattern.
    Sums all parsed digits in score variable
    :param current_line: str
    :return: int
    """
    score = 0
    pattern = r'\d'
    matched_digits = re.findall(pattern, current_line)
    for digit in matched_digits:
        score += int(digit)
    return score


def info_processing(current_name, current_score):
    """
    Store the information about the person only if the list of participants contains the name of the person.
    If received the same person more than once just added distance to his old distance.
    :param current_name: str
    :param current_score: int
    """
    global participants
    global race
    if current_name in participants:
        if current_name in race.keys():
            race[current_name] += current_score
        else:
            race[current_name] = current_score


def output():
    """
    Print the top 3 racers ordered by distance in descending.
    """
    global race
    places = ['1st', '2nd', '3rd']
    names = []
    sorted_by_points = sorted(race.items(), key=lambda x: -x[1])
    for kvp in list(sorted_by_points)[0:3]:
        names.append(kvp[0])

    for idx in range(len(places)):
        print(f'{places[idx]} place: {names[idx]}')


participants = input().split(', ')
race = {}

while True:

    line = input()

    if line == 'end of race':
        break

    participant_name = find_all_letters(line)
    participant_score = find_all_digits(line)
    info_processing(participant_name, participant_score)

output()
