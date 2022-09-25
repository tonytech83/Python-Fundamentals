targets = []

for value in input().split(' '):
    targets.append(int(value))

while True:

    command = input().split(' ')

    # check if command is Shoot
    if command[0] == 'Shoot':
        index = int(command[1])
        value = int(command[2])
        if 0 <= index < len(targets):
            targets[index] -= value
            if targets[index] <= 0:
                targets.pop(index)

    # check if command is Add
    elif command[0] == 'Add':
        index = int(command[1])
        value = int(command[2])
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print('Invalid placement!')

    # check if command is Strike
    elif command[0] == 'Strike':
        index = int(command[1])
        radius = int(command[2])
        left_radius = index - radius
        right_radius = index + radius
        if left_radius >= 0 and right_radius < len(targets):
            del targets[left_radius: right_radius + 1]
        else:
            print('Strike missed!')

    elif command[0] == 'End':
        print(*targets, sep='|')
        break
