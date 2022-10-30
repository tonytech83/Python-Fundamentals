def init_user(book: dict, command: str):
    force_side, force_user = command.split(' | ')
    if force_side not in book and not user_exists(book, force_user):
        book[force_side] = []
        book[force_side].append(force_user)
    elif not user_exists(book, force_user):
        book[force_side].append(force_user)


def move_user(book: dict, command: str):
    force_user, force_side = command.split(' -> ')
    # If there is no such force user and no such force side ->
    # create new force side and add the force user to the corresponding side.
    if force_side not in book and not user_exists(book, force_user):
        book[force_side] = []
        book[force_side].append(force_user)
    # If there is no such force user in any force side -> add the force user to the corresponding force side.
    elif not user_exists(book, force_user):
        if force_side not in book:
            book[force_side] = []
        book[force_side].append(force_user)
    # If there is such force user already -> change their side.
    elif user_exists(book, force_user):
        remove_user(book, force_user)
        if force_side not in book:
            book[force_side] = []
        book[force_side].append(force_user)

    print(f'{force_user} joins the {force_side} side!')


def user_exists(book: dict, user: str):
    for users_list in book.values():
        if user in users_list:
            return True

    return False


def remove_user(book: dict, user: str):
    for side, users in book.items():
        if user in users:
            book[side].remove(user)


forces_book = {}

while True:
    line = input()
    if line == 'Lumpawaroo':
        break
    if '|' in line:
        init_user(forces_book, line)
    elif '->' in line:
        move_user(forces_book, line)

for force, users in forces_book.items():
    if len(users) > 0:
        print(f'Side: {force}, Members: {len(users)}')
        for user in users:
            print(f'! {user}')
