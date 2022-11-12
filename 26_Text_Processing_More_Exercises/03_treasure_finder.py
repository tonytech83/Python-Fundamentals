import re


def message_decryption(current_line):
    global key
    message = ''
    internal_key = key.copy()
    for char in current_line:
        idx = internal_key.pop(0)
        message += chr(ord(char) - idx)
        if not internal_key:
            internal_key = key.copy()
    return message


def treasure_coordinates(message):
    pattern = re.findall(r'&(\w+)+&', message)
    current_treasure = [x for x in pattern if x.isalpha()]
    treasure_type = ''.join(current_treasure)

    treasure_coord = ''
    idx_of_hash = message.index('<')
    idx_of_asterix = message.index('>')
    for digit in range(idx_of_hash + 1, idx_of_asterix):
        treasure_coord += message[digit]

    return treasure_type, treasure_coord


key = [int(x) for x in input().split()]

while True:
    line = input()
    if line == 'find':
        break
    hidden_message = message_decryption(line)
    treasure, coordinates = treasure_coordinates(hidden_message)
    print(f'Found {treasure} at {coordinates}')
