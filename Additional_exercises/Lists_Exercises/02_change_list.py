def delete(received_command):
    """
    This function removes element from numbers list if it exists.
    :param received_command: str
    """
    global numbers
    element = int(received_command[1])
    numbers = [num for num in numbers if num != element]


def insert(received_command):
    """
    This function inserts element in numbers list.
    :param received_command: str
    """
    global numbers
    element = int(received_command[1])
    position = int(received_command[2])
    numbers.insert(position, element)


def output():
    """
    This function takes care of console print.
    """
    global numbers
    if command == 'Odd':
        print(*(x for x in numbers if x % 2 != 0))
    else:
        print(*(x for x in numbers if x % 2 == 0))


numbers = [int(x) for x in input().split()]

stop_commands = ['Odd', 'Even']

while True:
    command = input()
    if command in stop_commands:
        break

    current_command = command.split()
    event = current_command[0]

    if event == 'Delete':
        delete(current_command)
    elif event == 'Insert':
        insert(current_command)

output()
