data = [x for x in input()]

my_dict = {}

for letter in data:
    if letter != ' ':
        if letter not in my_dict:
            my_dict[letter] = 1
        else:
            my_dict[letter] += 1

for key, value in my_dict.items():
    print(f'{key} -> {value}')
