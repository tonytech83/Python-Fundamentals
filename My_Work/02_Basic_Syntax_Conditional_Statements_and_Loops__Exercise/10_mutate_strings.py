string_1 = input()
string_2 = input()

mutate_list = list(string_1)

for letter in range(len(string_1)):
    if mutate_list[letter] != string_2[letter]:
        mutate_list[letter] = string_2[letter]
        print(*mutate_list, sep='')
