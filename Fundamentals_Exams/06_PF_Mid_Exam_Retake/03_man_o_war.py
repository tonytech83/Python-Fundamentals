def fire(current_command):
    global warship
    global have_winner
    section = int(current_command[1])
    damage = int(current_command[2])
    if section in range(len(warship)):
        warship[section] -= damage
        if warship[section] <= 0:
            have_winner = True
            print('You won! The enemy ship has sunken.')
            return have_winner


def defend(current_command):
    global pirate_ship
    global have_winner
    start_section = int(current_command[1])
    end_section = int(current_command[2])
    damage = int(current_command[3])
    if start_section in range(len(pirate_ship)) and end_section in range(len(pirate_ship)):
        for section in range(start_section, end_section + 1):
            pirate_ship[section] -= damage
            if pirate_ship[section] <= 0:
                have_winner = True
                print('You lost! The pirate ship has sunken.')
                return have_winner


def repair(current_command):
    global pirate_ship
    section = int(current_command[1])
    given_health = int(current_command[2])
    if section in range(len(pirate_ship)):
        pirate_ship[section] += given_health
        if pirate_ship[section] > section_maximum_health:
            pirate_ship[section] = section_maximum_health


def status():
    global pirate_ship
    twenty_percents = section_maximum_health * 0.2
    sections_need_repair = len([section for section in pirate_ship if section < twenty_percents])
    print(f'{sections_need_repair} sections need repair.')


def battle():
    while True:
        command = input()

        if command == 'Retire' or have_winner:
            break

        current_command = command.split()
        event = current_command[0]

        if event == 'Fire':
            fire(current_command)

        elif event == 'Defend':
            defend(current_command)

        elif event == 'Repair':
            repair(current_command)

        elif event == 'Status':
            status()


have_winner = False
pirate_ship = list(map(int, input().split('>')))
warship = list(map(int, input().split('>')))
section_maximum_health = int(input())

battle()

if not have_winner:
    print(f'Pirate ship status: {sum(pirate_ship)}\nWarship status: {sum(warship)}')
