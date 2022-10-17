def attack(matrix, attacks_lst, destroyed_ships):
    for action in attacks_lst:
        current_action = action.split('-')
        row = int(current_action[0])
        col = int(current_action[1])
        if matrix[row][col] > 0:
            matrix[row][col] -= 1
            if matrix[row][col] == 0:
                destroyed_ships += 1
    return destroyed_ships


rows = int(input())

battlefield = []
destroyed_ships = 0

for _ in range(rows):
    battlefield.append([int(x) for x in input().split(' ')])

attacks = list(map(str, input().split(' ')))

print(attack(battlefield, attacks, destroyed_ships))
