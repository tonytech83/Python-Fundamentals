def shoot_at_target(targets, idx, power):
    if idx in range(len(targets)):
        targets[idx] -= power
        if targets[idx] <= 0:
            targets.pop(idx)
    return targets


def add_to_target(targets, idx, value):
    if idx in range(len(targets)):
        targets.insert(idx, value)
    else:
        print('Invalid placement!')
    return targets


def strike_to_target(targets, idx, radius):
    left_radius = idx - radius
    right_radius = idx + radius
    if left_radius in range(len(targets)) and right_radius in range(len(targets)):
        del targets[left_radius:right_radius + 1]
    else:
        print('Strike missed!')
    return targets


def manipulating_targets(targets):
    while True:
        command = input()

        if command == 'End':
            break

        event, index, value = command.split()

        if event == 'Shoot':
            shoot_at_target(targets, int(index), int(value))
        elif event == 'Add':
            add_to_target(targets, int(index), int(value))
        elif event == 'Strike':
            strike_to_target(targets, int(index), int(value))

    return targets


sequence_of_targets = [int(x) for x in input().split()]

targets_after_manipulation = manipulating_targets(sequence_of_targets)
print(*targets_after_manipulation, sep='|')
