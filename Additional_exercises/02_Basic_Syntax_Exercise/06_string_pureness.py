n = int(input())

not_pure_chr = False

for string in range(n):

    current_string = input()

    for letter in current_string:
        if letter == ',' or letter == '.' or letter == '_':
            not_pure_chr = True
            break
        else:
            continue

    if not_pure_chr:
        print(f'{current_string} is not pure!')
        not_pure_chr = False

    else:
        print(f'{current_string} is pure.')
