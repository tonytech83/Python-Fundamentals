number = int(input())
zero_or_one = input()

binary_text = 'ones'
if zero_or_one == 0:
    binary_text = 'zeroes'

binary_number = bin(number)[2:]
binary_digit_count = binary_number.count(zero_or_one)

print(f'{number} - > {binary_number}')
print(f'We have {binary_digit_count} {binary_text}')
