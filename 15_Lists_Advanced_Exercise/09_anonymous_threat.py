def merge(current_command):
    global single_string
    merged = []
    start_idx = int(current_command[1])
    end_idx = int(current_command[2])

    if start_idx < 0:
        start_idx = 0
    if end_idx > len(single_string) - 1:
        end_idx = len(single_string) - 1

    for idx in range(start_idx, end_idx + 1):
        merged.append(single_string[idx])

    single_string = [x for x in single_string if x not in merged]
    merged = ''.join(merged)
    single_string.insert(start_idx, merged)


def divide(current_command):
    global single_string
    idx = int(current_command[1])
    partitions = int(current_command[2])
    element = single_string[idx]
    new_sub_stings = []
    if len(element) % partitions == 0:
        sub_element = ''
        take_letters = len(element) // partitions
        for _ in range(partitions):
            sub_element += element[:take_letters]
            element = element[take_letters:]
            new_sub_stings.append(sub_element)
            sub_element = ''
    else:
        sub_element = ''
        take_element = len(element) // partitions
        for _ in range(partitions - 1):
            for sub in range(len(element) // partitions):
                sub_element += element[:take_element]
                element = element[take_element:]
                new_sub_stings.append(sub_element)
                sub_element = ''
        new_sub_stings.append(element)

    single_string.remove(single_string[idx])
    for sub_string in new_sub_stings:
        single_string.insert(idx, sub_string)
        idx += 1


single_string = [x for x in input().split()]

while True:
    command = input().split()
    if command[0] == '3:1':
        break
    event = command[0]
    if event == 'merge':
        merge(command)
    elif event == 'divide':
        divide(command)

print(*single_string, sep=' ')
