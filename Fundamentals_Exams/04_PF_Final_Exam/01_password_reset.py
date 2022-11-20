def take_odd_characters():
    """
    Takes only the characters at odd indices and concatenates them to obtain the new raw password and then prints it.
    :return: str
    """
    global text
    odd_text = ''

    for idx in range(len(text)):
        if idx % 2 != 0:
            odd_text += text[idx]
    text = odd_text
    return text


def cut_string(current_data):
    """
    Gets the substring with the given length starting from the given index from the password and
    removes its first occurrence, then prints the password on the console.
    :param current_data: str
    :return: str
    """
    global text

    idx = int(current_data[1])
    length = int(current_data[2])
    substring = text[idx:(idx + length)]

    if substring in text:
        text = text.replace(substring, '', 1)
    return text


def replace_string(current_data):
    """
    If the raw password contains the given substring, replaces all of its occurrences with
    the substitute text given and prints the result.
    :param current_data: str
    :return: str
    """
    global text
    given_string = current_data[1]
    substitute_text = current_data[2]

    if given_string in text:
        text = text.replace(given_string, substitute_text)
        return text
    else:
        return 'Nothing to replace!'


text = input()

while True:
    command = input()
    if command == 'Done':
        break

    data = command.split()
    action = data[0]
    if action == 'TakeOdd':
        print(take_odd_characters())
    elif action == 'Cut':
        print(cut_string(data))
    elif action == 'Substitute':
        print(replace_string(data))

print(f'Your password is: {text}')
