def memory_game(elements):
    move_counter = 0
    while True:
        command = input()
        if command == 'end':
            break

        move_counter += 1

        current_command = command.split()
        first_idx = int(current_command[0])
        second_idx = int(current_command[1])
        if first_idx == second_idx or first_idx not in range(len(elements)) or second_idx not in range(len(elements)):
            mid_of_elements = len(elements) // 2
            for _ in range(2):
                elements.insert(mid_of_elements, f'-{move_counter}a')
            print('Invalid input! Adding additional elements to the board')
        else:
            if elements[first_idx] == elements[second_idx]:
                element = elements[first_idx]
                if first_idx > second_idx:
                    elements.pop(first_idx)
                    elements.pop(second_idx)
                else:
                    elements.pop(second_idx)
                    elements.pop(first_idx)
                print(f'Congrats! You have found matching elements - {element}!')
            else:
                print('Try again!')

        if not elements:
            print(f'You have won in {move_counter} turns!')
            break

    return elements


sequence_of_elements = [x for x in input().split()]

current_sequence_state = memory_game(sequence_of_elements)

if sequence_of_elements:
    print('Sorry you lose :(')
    print(*current_sequence_state, sep=' ')
