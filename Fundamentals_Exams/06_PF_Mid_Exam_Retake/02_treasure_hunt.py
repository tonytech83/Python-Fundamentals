def loot(command, initial_loot):
    """
    :param command: receive input from customer
    :param initial_loot: list of items received by customer
    :list current_lot: split the variable to list of items
    :list new_lot: exclude event (the first element) and add only the new items in new_lot.
    :return: initial_list after adding only non-contained items
    """
    current_lot = command.split()
    new_lot = current_lot[1:]
    # take all items one by one from new_lot list
    for new_item in new_lot:
        # if item not in initial_loot list insert the item at the beginning
        if item not in initial_loot:
            initial_loot.insert(0, new_item)
    return initial_loot


def drop(command, initial_loot):
    """
    :param command: receive input from customer
    :param initial_loot: list of items received by customer
    :list drop_event: split the variable to list of items
    :variable idx - the index of item which should be removed
    :return: initial_list after remove the item by index and add it at the end of the list
    """
    drop_event = command.split()
    idx = int(drop_event[1])
    # check if index is inside of initial_loot list.
    # if yes remove the item and add it at the end of the list
    if 0 <= idx <= len(initial_loot):
        removed_item = initial_loot.pop(idx)
        initial_loot.append(removed_item)
    return initial_loot


def steal(command, initial_loot):
    """
    :param command: receive input from customer
    :param initial_loot: list of items received by customer
    :list steal_event: split the variable to list of items
    :variable count: the count of items which should be removed
    :list stolen_items: contained all items removed from end of initial_loot list
    :return: print stolen_items list and return initial_loot
    """
    steal_event = command.split()
    count = int(steal_event[1])
    stolen_items = []
    # remove item per iteration in range of count and add it to stolen_items list
    for item in range(count):
        stolen_item = initial_loot.pop()
        stolen_items.insert(0, stolen_item)
        # check if initial_loot is empty
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

# check initial_loot list is empty
if not initial_loot:
    print('Failed treasure hunt.')
# if the initial_loot is not empty, take the length items one by one and add it to total_gain variable
else:
    total_gain = 0
    for item in initial_loot:
        total_gain += len(item)
    # delete the total length of elements in initial_loot list and divide it to length of initial_loot list
    # result is average gain
    average_gain = total_gain / len(initial_loot)
    print(f'Average treasure gain: {average_gain:.2f} pirate credits.')
