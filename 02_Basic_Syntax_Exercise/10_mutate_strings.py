first_string = input()
second_string = input()

mutate_string = list(first_string)

for letter in range(len(first_string)):
    if mutate_string[letter] != second_string[letter]:
        mutate_string[letter] = second_string[letter]
        print(*mutate_string, sep='')
