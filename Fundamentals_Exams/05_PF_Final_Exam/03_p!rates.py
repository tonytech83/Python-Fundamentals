def plunder_town(current_data):
    """
    This function decreasing amount of population and gold of town in targets with given amount.
    If any of those two values (population or gold) reaches zero, the town is disbanded and
    should be removed from targets dictionary.
    :param current_data: str
    """
    global targets
    current_town = current_data[1]
    killed_population = int(current_data[2])
    stolen_gold = int(current_data[3])

    targets[current_town][0] -= killed_population
    targets[current_town][1] -= stolen_gold

    print(f'{current_town} plundered! {stolen_gold} gold stolen, {killed_population} citizens killed.')

    if targets[current_town][0] <= 0 or targets[current_town][1] <= 0:
        del targets[current_town]
        print(f'{current_town} has been wiped off the map!')


def prosper_town(current_data):
    """
    This function increases the amount of gold for given town only if received amount is positive number.
    :param current_data: str
    """
    global targets
    current_town = current_data[1]
    add_gold = int(current_data[2])

    if add_gold < 0:
        print(f'Gold added cannot be a negative number!')
    else:
        targets[current_town][1] += add_gold
        print(f'{add_gold} gold added to the city treasury. {current_town} now has {targets[current_town][1]} gold.')


def output():
    """
    This function print the towns if left in targets dictionary.
    """
    global targets

    if len(targets):
        print(f'Ahoy, Captain! There are {len(targets)} wealthy settlements to go to:')
        for key, info in targets.items():
            print(f'{key} -> Population: {info[0]} citizens, Gold: {info[1]} kg')
    else:
        print('Ahoy, Captain! All targets have been plundered and destroyed!')


def action():
    """
    This function receiving lines of text representing events until the "End" command is given.
    Depending on the event, different functions are called.
    """
    while True:
        line = input()
        if line == 'End':
            output()
            break

        data = line.split('=>')
        event = data[0]

        if event == 'Plunder':
            plunder_town(data)
        elif event == 'Prosper':
            prosper_town(data)


targets = {}

while True:
    command = input()
    if command == 'Sail':
        action()
        break

    town, population, gold = command.split('||')

    if town not in targets:
        targets[town] = [int(population), int(gold)]
    else:
        targets[town][0] += int(population)
        targets[town][1] += int(gold)
