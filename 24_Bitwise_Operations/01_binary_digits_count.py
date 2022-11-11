number = int(input())
zero_or_one = int(input())
counter = 0

while number != 0:
    bit_reminder = number % 2
    if bit_reminder == zero_or_one:
        counter += 1
    number = number // 2

print(f'{counter}')
