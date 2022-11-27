import re


def find_pairs(current_text):
    """
    This function:
    - separates series in current_text by '&'
    - iterates through all matches and searches for matches with regex pattern
    - calling add_pairs func
    :param current_text: str
    """
    pairs = re.split('&', current_text)
    pairs_dict = {}

    for pair in pairs:
        pattern = r'([^&=?]*)=([^&=]*)'
        matches = re.findall(pattern, pair)
        add_pairs(matches, pairs_dict)

    output(pairs_dict)


def add_pairs(current_matches, current_dict):
    """
    This function add field and value to pairs_dict dictionary, if field exist append new value
    :param current_dict: dict
    :param current_matches: list
    """
    for match in current_matches:
        key = prepair(match[0])
        value = prepair(match[1])

        if key not in current_dict:
            current_dict[key] = []
            current_dict[key].append(value)
        else:
            current_dict[key].append(value)


def prepair(item):
    """
    This function receives filed or value and:
    - replaces '+' and '%20' with whitespace
    - strip whitespaces before/after extracted field and values
    - reduced multiple whitespaces to one inside field/key names
    :param item: str
    :return: str
    """
    item = item.replace(r'+', ' ')
    item = item.replace('%20', ' ')
    item = item.strip()
    item = re.sub(' +', ' ', item)
    return item


def output(current_dict):
    """
    This function for each input line, print on the console a line containing the processed string as follows:
    key=[value]nextkey=[another value] ... etc.
    :param current_dict: dict
    """
    for field, values in current_dict.items():
        print(f'{field}=[{", ".join(values)}]', end='')
    print()


while True:
    text = input()
    if text == 'END':
        break

    find_pairs(text)
