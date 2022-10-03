sequence_of_elements = input().split(' ')

moves_counter = 0

command = input()

while command != 'end':

    moves_counter += 1

    first_idx = int(command.split()[0])
    second_idx = int(command.split()[1])

    if (first_idx < 0 or second_idx < 0) or first_idx == second_idx\
            or first_idx >= len(sequence_of_elements) or second_idx >= len(sequence_of_elements):
        insert_idx = len(sequence_of_elements) // 2
        insert_obj = f'-{moves_counter}a'
        for _ in range(2):
            sequence_of_elements.insert(insert_idx, insert_obj)
        print(f'Invalid input! Adding additional elements to the board')
    else:
        if sequence_of_elements[first_idx] == sequence_of_elements[second_idx]:
            print(f'Congrats! You have found matching elements - {sequence_of_elements[first_idx]}!')
            if first_idx > second_idx:
                sequence_of_elements.pop(first_idx)
                sequence_of_elements.pop(second_idx)
            else:
                sequence_of_elements.pop(second_idx)
                sequence_of_elements.pop(first_idx)

        else:
            print('Try again!')

    if not sequence_of_elements:
        print(f'You have won in {moves_counter} turns!')
        break

    command = input()

if command == 'end':
    print('Sorry you lose :(')
    print(*sequence_of_elements, sep=' ')
