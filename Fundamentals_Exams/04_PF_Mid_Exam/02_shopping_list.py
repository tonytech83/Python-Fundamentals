shop_list = input().split('!')

command = input()

while command != 'Go Shopping!':

    command = command.split(' ')
    command_type = command[0]
    item_one = command[1]

    if command_type == 'Urgent':
        if item_one not in shop_list:
            shop_list.insert(0, item_one)

    elif command_type == 'Unnecessary':
        if item_one in shop_list:
            shop_list.remove(item_one)

    elif command_type == 'Correct':
        item_two = command[2]
        if item_one in shop_list:
            for idx, value in enumerate(shop_list):
                if shop_list[idx] == item_one:
                    shop_list[idx] = item_two

    elif command_type == 'Rearrange':
        if item_one in shop_list:
            for idx, value in enumerate(shop_list):
                if shop_list[idx] == item_one:
                    shop_list.pop(idx)
                    shop_list.append(value)

    command = input()

print(*shop_list, sep=', ')
