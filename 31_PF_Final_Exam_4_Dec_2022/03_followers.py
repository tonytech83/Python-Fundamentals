def new_follower(current_data):
    global facebook_followers
    username = current_data[1]
    if username not in facebook_followers:
        facebook_followers[username] = [0, 0]


def like(current_data):
    global facebook_followers
    username = current_data[1]
    likes_count = current_data[2]
    if username not in facebook_followers:
        facebook_followers[username] = [int(likes_count), 0]
    else:
        facebook_followers[username][0] += int(likes_count)


def comment(current_data):
    global facebook_followers
    username = current_data[1]
    if username not in facebook_followers:
        facebook_followers[username] = [0, 1]
    else:
        facebook_followers[username][1] += 1


def blocked(current_data):
    global facebook_followers
    username = current_data[1]
    if username in facebook_followers:
        del facebook_followers[username]
    else:
        print(f"{username} doesn't exist.")


def output():
    global facebook_followers
    print(f'{len(facebook_followers)} followers')
    for user, info in facebook_followers.items():
        print(f'{user}: {sum(info)}')


facebook_followers = {}

while True:
    command = input()
    if command == 'Log out':
        break

    data = command.split(': ')
    event = data[0]

    if event == 'New follower':
        new_follower(data)
    elif event == 'Like':
        like(data)
    elif event == 'Comment':
        comment(data)
    elif event == 'Blocked':
        blocked(data)

output()
