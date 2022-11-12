def add_message(chat, message):
    new_message = message[1]
    return chat.append(new_message)


def delete_message(chat, message):
    message_to_remove = message[1]
    if message_to_remove in chat:
        chat.remove(message_to_remove)
    return chat


def edit_message(chat, message):
    old_message = message[1]
    new_message = message[2]
    if old_message in chat:
        idx_old_message = chat.index(old_message)
        chat.insert(idx_old_message, new_message)
        chat.pop(idx_old_message + 1)
    return chat


def pin_message(chat, message):
    message_to_pin = message[1]
    if message_to_pin in chat:
        chat.remove(message_to_pin)
        chat.append(message_to_pin)
    return chat


def spam_message(chat, messages):
    messages.remove('Spam')
    for message in messages:
        chat.append(message)
    return chat


chat_history = []

while True:

    command = input()

    if command == 'end':
        break

    current_command = command.split()
    event = current_command[0]

    if event == 'Chat':
        add_message(chat_history, current_command)

    elif event == 'Delete':
        delete_message(chat_history, current_command)

    elif event == 'Edit':
        edit_message(chat_history, current_command)

    elif event == 'Pin':
        pin_message(chat_history, current_command)

    elif event == 'Spam':
        spam_message(chat_history, current_command)

print('\n'.join(chat_history))
