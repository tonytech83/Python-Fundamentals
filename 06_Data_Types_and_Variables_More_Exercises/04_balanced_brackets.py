number_of_lines = int(input())

bracket_array = [None]

is_balanced = True

for line in range(number_of_lines):

    char = input()

    if char == "(" or char == ")":
        if char == bracket_array[-1]:
            is_balanced = False
            break
        bracket_array.append(char)
    else:
        continue

if is_balanced and bracket_array[1] == "(":
    print(f'BALANCED')
else:
    print('UNBALANCED')
