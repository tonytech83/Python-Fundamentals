def contains(current_data):
    """
    This func checks if the activation_key string contains substring.
    :param current_data: str
    :return: str
    """
    global activation_key
    substring = current_data[1]

    if substring in activation_key:
        return f'{activation_key} contains {substring}'
    return 'Substring not found!'


def flips(current_data):
    """
    This func changes the substring between the given indices (the end index is exclusive) to upper or lower case
    and then prints the activation key.
    :param current_data: str
    :return: str
    """
    global activation_key
    flip_type = current_data[1]
    start_idx = int(current_data[2])
    end_idx = int(current_data[3])
    left_side = activation_key[:start_idx]
    right_side = activation_key[end_idx:]
    middle_side = activation_key[start_idx:end_idx]

    if flip_type == 'Upper':
        middle_side = middle_side.upper()
    elif flip_type == 'Lower':
        middle_side = middle_side.lower()

    activation_key = left_side + middle_side + right_side

    return activation_key


def slices(current_data):
    """
    This func deletes the characters between the start and end indices (the end index is exclusive)
    and prints the activation key.
    :param current_data: str
    :return: str
    """
    global activation_key
    start_idx = int(current_data[1])
    end_idx = int(current_data[2])

    activation_key = activation_key[:start_idx] + activation_key[end_idx:]

    return activation_key


activation_key = input()

while True:
    command = input()
    if command == 'Generate':
        break

    data = command.split('>>>')
    event = data[0]

    if event == 'Contains':
        print(contains(data))

    elif event == 'Flip':
        print(flips(data))

    elif event == 'Slice':
        print(slices(data))

print(f'Your activation key is: {activation_key}')
