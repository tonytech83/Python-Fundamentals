def add_stop(world_tour):
    """
    If True function returns modified all_stops string
    :param world_tour: str
    :return all_stops
    """
    global all_stops
    idx = int(world_tour[1])
    new_stop = world_tour[2]
    if idx in range(len(all_stops)):
        all_stops = all_stops[:idx] + new_stop + all_stops[idx:]
        return all_stops
    return all_stops


def remove_stop(world_tour):
    """
    If True function returns modified all_stops string
    :param world_tour: str
    :return: all_stops
    """
    global all_stops
    start_idx = int(world_tour[1])
    end_idx = int(world_tour[2])
    if start_idx in range(len(all_stops)) and end_idx in range(len(all_stops)):
        all_stops = all_stops[:start_idx] + all_stops[end_idx + 1:]
        return all_stops
    return all_stops


def switch_stop(world_tour):
    """
    If True function returns modified all_stops string
    :param world_tour: str
    :return: all_stops
    """
    global all_stops
    old_destination = world_tour[1]
    new_destination = world_tour[2]
    if old_destination in all_stops:
        all_stops = all_stops.replace(old_destination, new_destination)
        return all_stops
    return all_stops


all_stops = input()

while True:
    command = input()

    if command == 'Travel':
        break

    tour = command.split(':')

    if tour[0] == 'Add Stop':
        print(add_stop(tour))
    elif tour[0] == 'Remove Stop':
        print(remove_stop(tour))
    elif tour[0] == 'Switch':
        print(switch_stop(tour))

print(f'Ready for world tour! Planned stops: {all_stops}')
