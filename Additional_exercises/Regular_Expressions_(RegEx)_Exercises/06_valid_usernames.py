import re

splitters = r'[\s\/\\\(\)]'
split_line = re.split(splitters, input())

usernames = []

for username in split_line:
    pattern = r'^[A-Za-z][a-zA-Z0-9_]{2,24}$'  # \b([A-Za-z][\w]{2,24})\b
    match = re.match(pattern, username)
    if match:
        usernames.append(match.group(0))

biggest_sum = 0
result = ()

for idx in range(0, len(usernames) - 1):
    couple_sum = len(usernames[idx]) + len(usernames[idx + 1])
    if couple_sum > biggest_sum:
        biggest_sum = couple_sum
        result = (usernames[idx], usernames[idx + 1])

print('\n'.join(result))
