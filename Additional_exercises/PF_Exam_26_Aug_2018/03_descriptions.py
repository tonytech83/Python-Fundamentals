import re


def name_validation(current_row):
    """
    This func validates name of person with following requirements:
    - a string "name is" after which a single space and a name (first name and last name), separated by single space.
    Both names should start with capital letter.
    :param current_row: str
    :return: boolean
    """
    global full_name

    name_pattern = r'name\sis\s(?P<name>[A-Z][a-z]+\s[A-Z][a-z]+)'
    match = re.search(name_pattern, current_row)

    if match:
        full_name = match.group('name')
        return True
    return False


def age_validation(current_row):
    """
    This func validates age of person with following requirements:
    - single space before and after that two digits representing the person's age after which we have single space
    and the word "years". A valid age is between >9 and age<100
    :param current_row: str
    :return: boolean
    """
    global person_age

    age_pattern = r'\s(?P<age>\d{2})\s'
    match = re.search(age_pattern, current_row)

    if match:
        if 9 < int(match.group('age')) < 100:
            person_age = match.group('age')
            return True
    return False


def birth_validation(current_row):
    """
    This func validates birthdate of person with following requirements:
    - birthday date - before the date we should have the word "on" after that single space and
    then date in exact format dd-mm-yyyy (months will be digits and the date should be separated with "-" {dd-mm-yyyy})
    - Every description should end with '.'(dot) after the date of birth.
    :param current_row: str
    :return: boolean
    """
    global birthdate

    date_pattern = r'on\s(?P<date>\d{2}-\d{2}-\d{4}).'
    match = re.search(date_pattern, current_row)

    if match:
        birthdate = match.group('date')
        return True
    return False


def output():
    """
    This func prints all valid descriptions from persons_db
    """
    global persons_db

    if persons_db:
        for key, value in persons_db.items():
            print(f'Name of the person: {key}.')
            print(f'Age of the person: {value[0]}.')
            print(f'Birthdate of the person: {value[1]}.')
    else:
        print('DB is empty')


persons_db = {}

while True:
    row = input()
    if row == 'make migrations':
        output()
        break
    full_name = ''
    person_age = ''
    birthdate = ''
    if name_validation(row) and age_validation(row) and birth_validation(row):
        persons_db[full_name] = [person_age, birthdate]


