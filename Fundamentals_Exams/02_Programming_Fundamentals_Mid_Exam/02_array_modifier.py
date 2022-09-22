array = []

for digit in input().split(' '):
    array.append(int(digit))

while True:

    command = []

    for _ in input().split(' '):
        command.append(_)

    if command[0] == 'end':
        break

    if command[0] == 'decrease':
        for digit in range(len(array)):
            array[digit] -= 1
    else:

        first = int(command[1])
        second = int(command[2])

        if command[0] == 'swap':
            array[first], array[second] = array[second], array[first]

        if command[0] == 'multiply':
            array[first] = int(array[first]) * int(array[second])

print(*array, sep=', ')
