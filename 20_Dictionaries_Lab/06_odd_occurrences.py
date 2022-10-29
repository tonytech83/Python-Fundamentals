words_sequence = input().split()
my_dict = {}

for word in words_sequence:
    word_lower = word.lower()
    if word_lower not in my_dict:
        my_dict[word_lower] = 1
    else:
        my_dict[word_lower] += 1

for key, value in my_dict.items():
    if my_dict[key] % 2 != 0:
        print(f'{key}', end=' ')
