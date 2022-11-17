def add_piece(current_command):
    global pieces
    new_piece = current_command[1]
    new_composer = current_command[2]
    new_key = current_command[3]
    if new_piece in pieces:
        print(f'{new_piece} is already in the collection!')
    else:
        pieces[new_piece] = []
        pieces[new_piece].append(new_composer)
        pieces[new_piece].append(new_key)
        print(f'{new_piece} by {new_composer} in {new_key} added to the collection!')


def remove_piece(current_command):
    global pieces
    piece_for_remove = current_command[1]
    if piece_for_remove in pieces:
        del pieces[piece_for_remove]
        print(f'Successfully removed {piece_for_remove}!')
    else:
        print(f'Invalid operation! {piece_for_remove} does not exist in the collection.')


def change_key(current_command):
    global pieces
    piece_to_update = current_command[1]
    new_key = current_command[2]
    if piece_to_update in pieces:
        pieces[piece_to_update][1] = new_key
        print(f'Changed the key of {piece_to_update} to {new_key}!')
    else:
        print(f'Invalid operation! {piece_to_update} does not exist in the collection.')


number_of_pieces = int(input())

pieces = {}

for _ in range(number_of_pieces):
    piece, composer, key = input().split('|')
    if piece not in pieces:
        pieces[piece] = []
    pieces[piece].append(composer)
    pieces[piece].append(key)

while True:
    command = input().split('|')
    event = command[0]
    if event == 'Stop':
        break
    elif event == 'Add':
        add_piece(command)
    elif event == 'Remove':
        remove_piece(command)
    elif event == 'ChangeKey':
        change_key(command)

for key, value in pieces.items():
    print(f'{key} -> Composer: {value[0]}, Key: {value[1]}')
