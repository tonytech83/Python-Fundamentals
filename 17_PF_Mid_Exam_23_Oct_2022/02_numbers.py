def add_value(sequence, action):
    value = int(action[1])
    sequence.append(value)
    return sequence


def remove_value(sequence, action):
    value = int(action[1])
    if value in sequence:
        sequence.remove(value)
    return sequence


def replace_value(sequence, action):
    value = int(action[1])
    replacement = int(action[2])
    if value in sequence:
        value_idx = sequence.index(value)
        sequence.insert(value_idx, replacement)
        sequence.pop(value_idx + 1)
    return sequence


def collapse_value(sequence, action):
    global sequence_of_numbers
    value = int(action[1])
    sequence_of_numbers = [x for x in sequence if x >= value]


sequence_of_numbers = [int(x) for x in input().split()]

while True:

    command = input()

    if command == 'Finish':
        break

    current_command = command.split()
    event = current_command[0]

    if event == 'Add':
        add_value(sequence_of_numbers, current_command)

    elif event == 'Remove':
        remove_value(sequence_of_numbers, current_command)

    elif event == 'Replace':
        replace_value(sequence_of_numbers, current_command)

    elif event == 'Collapse':
        collapse_value(sequence_of_numbers, current_command)

print(*sequence_of_numbers, sep=' ')
