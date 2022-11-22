def add_element(current_command):
    """
    Adds element at the specified index (elements right from this position inclusively are shifted to the right).
    :param current_command: str
    """
    global numbers
    idx = int(current_command[1])
    element = int(current_command[2])
    numbers.insert(idx, element)


def add_many(current_command):
    """
    Adds a set of elements at the specified index.
    :param current_command: str
    """
    global numbers
    idx = int(current_command[1])
    elements_set = current_command[2:]
    for digit in range(len(elements_set)):
        numbers.insert(idx, int(elements_set[digit]))
        idx += 1


def contains_element(current_command):
    """
    This function returns the index of the first occurrence of the specified element (if exists) in the array or
    -1 if the element is not found.
    :param current_command: str
    :return: str
    """
    global numbers
    element = int(current_command[1])
    if element in numbers:
        return numbers.index(element)
    return '-1'


def remove_element(current_command):
    """
    This function removes the element at the specified index.
    :param current_command: str
    """
    global numbers
    idx = int(current_command[1])
    if idx in range(len(numbers)):
        numbers.pop(idx)


def shift_position(current_command):
    """
    This func shifts every element of the array the number of positions to the left (with rotation).
    :param current_command: str
    """
    global numbers
    position = int(current_command[1])
    for _ in range(position):
        element = numbers.pop(0)
        numbers.append(element)


def sum_pairs():
    """
    This func sums the elements in the array by pairs (first + second, third + fourth, …).
    :return:
    """
    global numbers
    if len(numbers) % 2 == 0:
        numbers = [numbers[x] + numbers[x + 1] for x in range(0, len(numbers), 2)]
    else:
        last_num = numbers[-1]
        numbers = [numbers[x] + numbers[x + 1] for x in range(0, len(numbers) - 1, 2)]
        numbers.append(last_num)


numbers = [int(x) for x in input().split()]

while True:
    command = input()
    if command == 'print':
        print(numbers)
        break
    data = command.split()
    event = data[0]

    if event == 'add':
        add_element(data)
    elif event == 'addMany':
        add_many(data)
    elif event == 'contains':
        print(contains_element(data))
    elif event == 'remove':
        remove_element(data)
    elif event == 'shift':
        shift_position(data)
    elif event == 'sumPairs':
        sum_pairs()
