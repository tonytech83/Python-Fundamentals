number = int(input())
binary_digit = input()

binary_text = 'ones'
if binary_digit == 0:
    binary_text = 'zeroes'

binary_number = bin(number)[2:]
binary_digit_count = binary_number.count(binary_digit)

print(f'{number} - > {binary_number}')
print(f'We have {binary_digit_count} {binary_text}')
