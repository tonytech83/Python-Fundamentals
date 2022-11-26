string = input()

numbers_list = [int(x) for x in string if x.isdigit()]
non_numbers = ''.join([x for x in string if not x.isdigit()])

take_list = [x for idx, x in enumerate(numbers_list) if idx % 2 == 0]
skip_list = [x for idx, x in enumerate(numbers_list) if idx % 2 != 0]

result_string = ''
total_skip = 0

for idx in range(len(take_list)):
    take_chars = take_list[idx]
    skip_chars = skip_list[idx]

    result_string += non_numbers[total_skip:(total_skip + take_chars)]
    total_skip += skip_chars + take_chars

print(result_string)
