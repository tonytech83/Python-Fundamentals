def insert_space(current_data, ):
    """
    This function inserts a single space at the given index.
    :param current_data: str
    :return: str
    """
    global concealed_message
    idx = int(current_data[1])
    concealed_message = concealed_message[:idx] + ' ' + concealed_message[idx:]

    return concealed_message


def reverse_substring(current_data):
    """
    This function manipulates the parameter concealed_message if:
    - the message contains the given substring, cut it out, reverse it and add it at the end of the message.
    - else return 'error'
    - The operation should replace only the first occurrence of the given substring.
    :param current_data: str
    :return: str
    """
    global concealed_message
    substring = current_data[1]
    if substring in concealed_message:
        reversed_substring = substring[::-1]
        concealed_message = concealed_message.replace(substring, '', 1) + reversed_substring
        return concealed_message
    return 'error'


def change_string(current_data):
    """
    This function changes all occurrences of the given substring with the replacement text.
    :param current_data: str
    :return: string
    """
    global concealed_message
    substring = current_data[1]
    replacement = current_data[2]
    if substring in concealed_message:
        concealed_message = concealed_message.replace(substring, replacement)

    return concealed_message


concealed_message = input()

while True:
    instruction = input()
    if instruction == 'Reveal':
        break

    data = instruction.split(':|:')

    if data[0] == 'InsertSpace':
        print(insert_space(data))
    elif data[0] == 'Reverse':
        print(reverse_substring(data))
    elif data[0] == 'ChangeAll':
        print(change_string(data))

print(f'You have a new text message: {concealed_message}')
