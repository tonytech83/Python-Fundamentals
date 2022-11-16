def move_letters(current_data):
    global encrypted_message
    number = int(current_data[1])
    encrypted_message = encrypted_message[number:] + encrypted_message[:number]


def insert_letter(current_data):
    global encrypted_message
    idx = int(current_data[1])
    value = str(current_data[2])
    encrypted_message = encrypted_message[:idx] + value + encrypted_message[idx:]


def change_all(current_data):
    global encrypted_message
    substring = current_data[1]
    replacement = current_data[2]
    encrypted_message = encrypted_message.replace(substring, replacement)


encrypted_message = input()

while True:
    command = input().split('|')
    if command[0] == 'Decode':
        break

    event = command[0]

    if event == 'Move':
        move_letters(command)
    elif event == 'Insert':
        insert_letter(command)
    elif event == 'ChangeAll':
        change_all(command)

print(f'The decrypted message is: {"".join(encrypted_message)}')
