numbers = [s for s in input().split()]
float_nums = [float(x) for x in numbers if '.' in x]
int_nums = [int(y) for y in numbers if '.' not in y]

all_nums = float_nums + int_nums

real_numbers = {}

for number in sorted(all_nums):
    if number not in real_numbers:
        real_numbers[number] = 0
    real_numbers[number] += 1

for key, value in real_numbers.items():
    print(f'{key} -> {value}')
