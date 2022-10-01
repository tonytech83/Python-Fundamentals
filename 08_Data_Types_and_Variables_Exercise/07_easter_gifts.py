gifts_list = [x for x in input().split()]

command = input()

while command != 'No Money':

    command = command.split()
    event = command[0]
    gift = command[1]

    if event == 'OutOfStock':
        for _ in range(gifts_list.count(gift)):
            idx = gifts_list.index(gift)
            gifts_list.insert(idx, 'None')
            gifts_list.pop(idx + 1)

    elif event == 'Required':
        index = int(command[2])
        if 0 <= index < len(gifts_list):
            gifts_list.insert(index, gift)
            gifts_list.pop(index + 1)

    elif event == 'JustInCase':
        gifts_list.pop()
        gifts_list.append(gift)

    command = input()

for gift in gifts_list:
    if gift != 'None':
        print(gift, end=' ')
