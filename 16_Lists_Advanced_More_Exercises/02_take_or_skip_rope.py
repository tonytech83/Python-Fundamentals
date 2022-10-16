def take_string(take_elements):
    global letters_lst
    global result_message
    for letter in range(take_elements):
        if not letters_lst:
            break
        result_message.append(letters_lst.pop(0))


def skip_string(skip_elements):
    global letters_lst
    global result_message
    for letter in range(skip_elements):
        if not letters_lst:
            break
        letters_lst.pop(0)


hidden_message = input()
result_message = []

numbers_lst = [int(x) for x in hidden_message if x.isdigit()]
letters_lst = [x for x in hidden_message if not x.isdigit()]

take_lst = [x for idx, x in enumerate(numbers_lst) if idx % 2 == 0]
skip_lst = [x for idx, x in enumerate(numbers_lst) if idx % 2 != 0]

for step in range(len(take_lst)):
    take = take_lst[step]
    skip = skip_lst[step]
    take_string(take)
    skip_string(skip)

print(*result_message, sep='')
