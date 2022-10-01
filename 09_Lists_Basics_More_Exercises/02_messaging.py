sequence_of_numbers = [x for x in input().split()]

received_string = [x for x in input()]

message = []

for number in sequence_of_numbers:

    current_idx = 0

    for digit in number:
        current_idx += int(digit)

    if current_idx >= len(received_string):
        current_idx -= len(received_string)

    message.append(received_string[current_idx])
    received_string.pop(current_idx)

print(*message, sep='')
