import re


def destroying(mine, start_idx, end_idx):
    """
    This function destroys all characters of mine. The mine also destroys n characters to the left and right of itself.
    n is determined by the absolute value of the subtraction of the ASCII codes of the first character and
    the second characters. Replace the destroyed characters with underscores – ‘_’.
    :param mine: str
    :param start_idx: int
    :param end_idx: int
    """
    global string
    first_char = mine[0]
    second_char = mine[1]

    power = abs(ord(first_char) - ord(second_char))
    left_explosion = start_idx - power
    right_explosion = end_idx + power - 1

    # if left explosion is outside of string, we set it to 0
    if left_explosion < 0:
        left_explosion = 0

    # if right explosion is outside of string, we set it to last index of string
    if right_explosion >= len(string):
        right_explosion = len(string) - 1

    string = [x for x in string]

    for char in range(left_explosion, right_explosion + 1):
        string[char] = '_'


string = input()

mine_pattern = r'<(.{2})>'
matches = re.finditer(mine_pattern, string)

for match in matches:
    start_index = match.span()[0]
    end_index = match.span()[1]
    destroying(match.group(1), start_index, end_index)

print(*string, sep='')
