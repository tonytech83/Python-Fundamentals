def collect(items_jornal, current_command):
    item = current_command[1]

    if not item in items_jornal:
        items_jornal.append(item)
    return items_jornal


def drop(items_jornal, current_command):
    item = current_command[1]
    if item in items_jornal:
        items_jornal.remove(item)
    return items_jornal


def combine_items(items_jornal, current_command):
    items = current_command[1].split(':')
    old_item = items[0]
    new_item = items[1]
    for idx, item in enumerate(items_jornal):
        if item == old_item:
            items_jornal.insert(idx + 1, new_item)
    return items_jornal


def renew(items_jornal, current_command):
    renew_item = current_command[1]
    for idx, item in enumerate(items_jornal):
        if item == renew_item:
            items_jornal.pop(idx)
            items_jornal.append(item)
            break
    return items_jornal


items_jornal = [x for x in input().split(', ')]

command = input()

while command != 'Craft!':
    current_command = command.split(' - ')
    event = current_command[0]

    if event == 'Collect':
        collect(items_jornal, current_command)

    elif event == 'Drop':
        drop(items_jornal, current_command)

    elif event == 'Combine Items':
        combine_items(items_jornal, current_command)

    elif event == 'Renew':
        renew(items_jornal, current_command)

    command = input()

print(*items_jornal, sep=', ')
