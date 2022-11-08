def length(current_username):
    if 3 <= len(current_username) <= 16:
        return True
    return False


def contain(current_username):
    for symbol in current_username:
        if symbol != '-' and symbol != '_' and not symbol.isdigit() and not symbol.isalpha():
            return False
    return True


usernames = input().split(', ')

valid_usernames = []

for username in usernames:
    if length(username) and contain(username):
        valid_usernames.append(username)

print(*valid_usernames, sep='\n')
