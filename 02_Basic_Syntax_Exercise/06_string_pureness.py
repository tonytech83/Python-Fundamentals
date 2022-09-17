strings_count = int(input())

for _ in range(strings_count):
    string = input()
    if ',' in string or '.' in string or '_' in string:
        print(f'{string} is not pure!')
    else:
        print(f'{string} is pure.')
