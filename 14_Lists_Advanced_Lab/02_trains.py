def add_people(current_command):
    global train
    people = int(current_command[1])
    train[-1] += people


def insert_people(current_command):
    global train
    wagon = int(current_command[1])
    people = int(current_command[2])
    train[wagon] += people


def remove_people(current_command):
    global train
    wagon = int(current_command[1])
    people = int(current_command[2])
    train[wagon] -= people


def main():
    command = input()

    while command != 'End':
        current_command = command.split(' ')
        event = current_command[0]

        if event == 'add':
            add_people(current_command)
        elif event == 'insert':
            insert_people(current_command)
        elif event == 'leave':
            remove_people(current_command)

        command = input()
    print(train)


number_wagons = int(input())
train = [0] * number_wagons
main()
