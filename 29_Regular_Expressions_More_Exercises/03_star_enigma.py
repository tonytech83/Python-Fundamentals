import re


def extract_info(message):
    """
    Try to find pattern in received message.
    Append name to proper key in planets dictionary
    :param message: str
    """

    global planets
    pattern = r'(?P<name>(?<=\@)[A-za-z]+)[^@:!\->]*:(?P<population>' \
              r'[\d]+)[^@:!\->]*!(?P<attack>[A|D])![^@:!\->]*->(?P<count>[\d]+)'

    info = re.findall(pattern, message)

    if info:
        name = info[0][0]
        attack = info[0][2]
        if attack == 'A':
            planets['A'].append(name)
        else:
            planets['D'].append(name)


def main(received_message):
    """
    Decrypt received message.
    Function count all the letters [s, t, a, r] in received message.
    Remove the count from the current ASCII value of each symbol of the encrypted message.
    Manipulates the dictionary planets
    :param received_message: str
    """

    global planets
    letters = ['s', 't', 'a', 'r']
    current_letters = []

    for ltr in received_message.lower():
        if ltr in letters:
            current_letters.append(ltr)

    decrypted_message = ''.join([chr(ord(x) - len(current_letters)) for x in received_message])

    extract_info(decrypted_message)


def output():
    """
    Print the decrypted information sorted by the planets ordered by name alphabetically.
    """
    global planets
    for key, value in planets.items():

        if key == 'A':
            sorted_value = sorted(value)
            print(f'Attacked planets: {len(value)}')
            for name in sorted_value:
                print(f'-> {name}')
        else:
            sorted_value = sorted(value)
            print(f'Destroyed planets: {len(value)}')
            for name in sorted_value:
                print(f'-> {name}')


planets = {'A': [], 'D': []}

number_of_messages = int(input())

for message in range(number_of_messages):
    current_message = input()

    main(current_message)

output()
