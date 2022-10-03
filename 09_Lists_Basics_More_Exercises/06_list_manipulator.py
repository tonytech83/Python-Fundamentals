def exchange(input_list, current_command):
    split_idx = int(current_command[1])
    if split_idx < 0 or split_idx >= len(input_list):
        print('Invalid index')
    else:
        first_part = input_list[:split_idx + 1]
        second_part = input_list[split_idx + 1:]
        input_list = second_part + first_part
    return input_list


def max_value(input_list, current_command):
    feature = current_command[1]
    current_idx = 'No matches'
    max_number = 0

    if feature == 'even':
        for idx, number in enumerate(input_list):
            if number % 2 == 0:
                if number >= max_number:
                    max_number = number
                    current_idx = idx
        print(current_idx)

    else:
        for idx, number in enumerate(input_list):
            if number % 2 != 0:
                if number >= max_number:
                    max_number = number
                    current_idx = idx
        print(current_idx)


def min_value(input_list, current_command):
    feature = current_command[1]
    current_idx = 'No matches'
    min_number = max(input_list)

    if feature == 'even':
        for idx, number in enumerate(input_list):
            if number % 2 == 0:
                if number <= min_number:
                    min_number = number
                    current_idx = idx
        print(current_idx)

    else:
        for idx, number in enumerate(input_list):
            if number % 2 != 0:
                if number <= min_number:
                    min_number = number
                    current_idx = idx
        print(current_idx)


def first(input_list, current_command):
    count = int(current_command[1])
    feature = current_command[2]

    if count > len(input_list):
        return print('Invalid count')

    elements = []

    if feature == 'even':
        for number in input_list:
            if number % 2 == 0:
                elements.append(number)
            if len(elements) == count:
                break
        print(elements)
    else:
        for number in input_list:
            if number % 2 != 0:
                elements.append(number)
            if len(elements) == count:
                break
        print(elements)


def last(input_list, current_command):
    count = int(current_command[1])
    feature = current_command[2]

    if count > len(input_list):
        return print('Invalid count')

    elements = []
    if feature == 'even':
        for number in reversed(input_list):
            if number % 2 == 0:
                elements.insert(0, number)
            if len(elements) == count:
                break
        print(elements)
    else:
        for number in reversed(input_list):
            if number % 2 != 0:
                elements.insert(0, number)
            if len(elements) == count:
                break
        print(elements)


input_list = [int(x) for x in input().split()]

command = input()

while command != 'end':

    current_command = command.split()
    event = current_command[0]

    if event == 'exchange':
        input_list = exchange(input_list, current_command)

    elif event == 'max':
        max_value(input_list, current_command)

    elif event == 'min':
        min_value(input_list, current_command)

    elif event == 'first':
        first(input_list, current_command)

    elif event == 'last':
        last(input_list, current_command)

    command = input()

print(input_list)
