def loot(command, initial_loot):
    current_lot = command.split()
    new_lot = current_lot[1:]
    for item in new_lot:
        if item not in initial_loot:
            initial_loot.insert(0, item)
    return initial_loot


def drop(command, initial_loot):
    drop_event = command.split()
    idx = int(drop_event[1])
    if 0 <= idx <= len(initial_loot):
        removed_item = initial_loot.pop(idx)
        initial_loot.append(removed_item)
    return initial_loot


def steal(command, initial_loot):
    steal_event = command.split()
    count = int(steal_event[1])
    stolen_items = []
    for item in range(count):
        stolen_item = initial_loot.pop()
        stolen_items.insert(0, stolen_item)
        if not initial_loot:
            break
    return print(*stolen_items, sep=', '), initial_loot


initial_loot = input().split('|')

command = input()

while command != 'Yohoho!':
    current_command = command.split()
    event = current_command[0]

    if event == 'Loot':
        loot(command, initial_loot)

    elif event == 'Drop':
        drop(command, initial_loot)

    elif event == 'Steal':
        steal(command, initial_loot)

    command = input()

if not initial_loot:
    print('Failed treasure hunt.')
else:
    total_gain = 0
    for item in initial_loot:
        total_gain += len(item)

    average_gain = total_gain / len(initial_loot)

    print(f'Average treasure gain: {average_gain:.2f} pirate credits.')
