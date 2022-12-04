def replacing(current_data):
    global string
    current_char = current_data[1]
    new_char = current_data[2]
    string = string.replace(current_char, new_char)
    return string


def cutting(current_data):
    global string
    start_idx = int(current_data[1])
    end_idx = int(current_data[2])
    if start_idx in range(len(string)) and end_idx in range(len(string)):
        string = string[:start_idx] + string[end_idx + 1:]
        return string
    return 'Invalid indices!'


def making(current_data):
    global string
    make_type = current_data[1]
    if make_type == 'Upper':
        string = string.upper()
        return string
    string = string.lower()
    return string


def checking(current_data):
    global string
    given_string = current_data[1]
    if given_string in string:
        return f'Message contains {given_string}'
    return f"Message doesn't contain {given_string}"


def summing(current_data):
    global string
    start_idx = int(current_data[1])
    end_idx = int(current_data[2])
    if start_idx in range(len(string)) and end_idx in range(len(string)):
        sub_string = [ord(char) for char in string[start_idx:end_idx + 1]]
        return f'{sum(sub_string)}'
    return 'Invalid indices!'


string = input()

while True:
    command = input()
    if command == 'Finish':
        break

    data = command.split()
    event = data[0]

    if event == 'Replace':
        print(replacing(data))
    elif event == 'Cut':
        print(cutting(data))
    elif event == 'Make':
        print(making(data))
    elif event == 'Check':
        print(checking(data))
    elif event == 'Sum':
        print(summing(data))
