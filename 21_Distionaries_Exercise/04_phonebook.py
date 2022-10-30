def searching(my_phonebook, my_searched_names):
    for name in my_searched_names:
        if name in my_phonebook:
            print(f'{name} -> {phonebook[name]}')
        else:
            print(f'Contact {name} does not exist.')


phonebook = {}

while True:
    data = input()
    if '-' not in data:
        break
    name, number = data.split('-')
    phonebook[name] = number

searched_names = []

for _ in range(int(data)):
    name = input()
    searched_names.append(name)

searching(phonebook, searched_names)
