targets = []

for value in input().split(' '):
    targets.append(int(value))

while True:

    command = input()

    if command == 'End':
        print(*targets, sep='|')
        break

    event, index, value = command.split()
    index = int(index)
    value = int(value)

    # check if command is Shoot
    if event == 'Shoot':
        if 0 <= index < len(targets):
            targets[index] -= value
            if targets[index] <= 0:
                targets.pop(index)

    # check if command is Add
    elif event == 'Add':
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print('Invalid placement!')

    # check if command is Strike
    elif event == 'Strike':
        left_radius = index - value
        right_radius = index + value
        if left_radius >= 0 and right_radius < len(targets):
            del targets[left_radius: right_radius + 1]
        else:
            print('Strike missed!')
