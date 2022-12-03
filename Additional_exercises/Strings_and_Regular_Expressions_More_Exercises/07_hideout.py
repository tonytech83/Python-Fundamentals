import re

the_map = input()

hideout_found = False

while True:

    if hideout_found:
        break

    char, count = input().split()
    pattern = rf'(\{char}+)'
    matches = re.finditer(pattern, the_map)

    for match in matches:
        if len(match.group()) >= int(count):
            print(f'Hideout found at index {match.span()[0]} and it is with size {len(match.group())}!')
            hideout_found = True
            break
