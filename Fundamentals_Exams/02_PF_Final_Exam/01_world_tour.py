def add_stop(world_tour):
    global all_stops
    idx = int(world_tour[1])
    new_stop = world_tour[2]
    if idx in range(len(all_stops)):
        before_idx = all_stops[:idx]
        after_idx = all_stops[idx:]
        all_stops = before_idx + new_stop + after_idx
    if all_stops:
        print(all_stops)


def remove_stop(world_tour):
    global all_stops
    start_idx = int(world_tour[1])
    end_idx = int(world_tour[2])
    if start_idx in range(len(all_stops)) and end_idx in range(len(all_stops)):
        left_part = all_stops[:start_idx]
        right_part = all_stops[end_idx + 1:]
        all_stops = left_part + right_part
    if all_stops:
        print(all_stops)


def switch_stop(world_tour):
    global all_stops
    old_destination = world_tour[1]
    new_destination = world_tour[2]
    if old_destination in all_stops:
        for _ in range(all_stops.count(old_destination)):
            all_stops = all_stops.replace(old_destination, new_destination)
    if all_stops:
        print(all_stops)


all_stops = input()

while True:
    command = input()

    if command == 'Travel':
        break

    tour = command.split(':')

    if tour[0] == 'Add Stop':
        add_stop(tour)
    elif tour[0] == 'Remove Stop':
        remove_stop(tour)
    elif tour[0] == 'Switch':
        switch_stop(tour)

print(f'Ready for world tour! Planned stops: {all_stops}')
