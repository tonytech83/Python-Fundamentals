def swap_command(current_data):
    global integers_list
    global command_counter

    start_idx = int(current_data[1])
    end_idx = int(current_data[2])
    command_counter += 1

    if start_idx in range(len(integers_list)) and end_idx in range(len(integers_list)):
        integers_list[start_idx], integers_list[end_idx] = integers_list[end_idx], integers_list[start_idx]
    return integers_list


def enumerate_command():
    global integers_list
    global command_counter

    command_counter += 1
    enumerated_list = [(i, e) for i, e in enumerate(integers_list)]

    return enumerated_list


def max_command():
    global integers_list
    global command_counter

    command_counter += 1
    return max(integers_list)


def min_command():
    global integers_list
    global command_counter

    command_counter += 1
    return min(integers_list)


def divisible_command(current_data):
    global command_counter

    command_counter += 1
    divisor = int(current_data[2])
    new_lst = [x for x in integers_list if x % divisor == 0]
    return new_lst


integers_list = [int(x) for x in input().split()]

command_counter = 0

while True:
    command = input()
    if command == 'end':
        print(command_counter)
        break

    data = command.split()
    event = data[0]

    if event == 'swap':
        print(swap_command(data))
    elif event == 'enumerate_list':
        print(enumerate_command())
    elif event == 'max':
        print(max_command())
    elif event == 'min':
        print(min_command())
    elif event == 'get_divisible':
        print(divisible_command(data))
