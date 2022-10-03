targets = []

for target in input().split(' '):
    targets.append(int(target))

hit_targets = 0

shot = input()

while shot != 'End':

    shot = int(shot)

    # continue if received invalid index
    if shot > len(targets) - 1:
        shot = input()
        continue

    # continue if target already shot
    if targets[shot] == -1:
        continue

    current_target = targets[shot]
    targets[shot] = -1
    hit_targets += 1

    for target in range(len(targets)):
        if targets[target] <= current_target and targets[target] != targets[shot]:
            targets[target] += current_target
        elif targets[target] > current_target and targets[target] != targets[shot]:
            targets[target] -= current_target

    shot = input()

print(f'Shot targets: {hit_targets} ->', *targets, sep=' ')
