import re


def demon_health(current_demon):
    """
    This function sums the ascii codes of all characters (excluding numbers (0-9),
    arithmetic symbols ('+', '-', '*', '/') and delimiter dot ('.')) and append demon total health to demons dict.
    :param current_demon: str
    """
    global demons
    pattern = r'(?P<name>[^\d\+\-\*\/\.])'
    matches = re.findall(pattern, rf'{current_demon}')
    health = 0
    for match in matches:
        health += sum([ord(x) for x in match])
    demons[current_demon].append(health)


def demon_damage(current_demon):
    """
    This function extracts all numbers with +/- with regex pattern_numbers and stored made all calculations.
    Also extracts symbols ('*' and '/') with regex pattern_symbols and stored them in symbols list
    Add results in demons dictionary
    :param current_demon: str
    """
    global demons
    pattern_numbers = r'(?P<numbers>[\-|+]?[\d]+\.?[\d]*)'
    pattern_symbols = r'(?P<symbols>[\*/])'
    numbers_matches = re.finditer(pattern_numbers, current_demon)
    symbols_matches = re.findall(pattern_symbols, current_demon)

    damage = 0
    for match in numbers_matches:
        damage += float((match.group('numbers')))

    symbols = [match for match in symbols_matches]
    for symbol in symbols:
        if symbol == '*':
            damage *= 2
        else:
            damage /= 2

    demons[current_demon].append(damage)


def output():
    """
    This function prints to console all demons sorted by their name in ascending order stored in demons dictionary
    """
    global demons
    for name, health_damage in sorted(demons.items(), key=lambda kvp: kvp[0]):
        print(f'{name} - {health_damage[0]} health, {health_damage[1]:.2f} damage')


data = [x.strip(' ') for x in input().split(',')]
demons = {}

for demon in data:
    demons[demon] = []
    demon_health(demon)
    demon_damage(demon)

output()
