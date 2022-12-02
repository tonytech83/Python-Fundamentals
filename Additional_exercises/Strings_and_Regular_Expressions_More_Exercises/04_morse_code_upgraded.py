letters = input().split('|')

message = ''

for letter in letters:
    current_letter = letter.count('1') * 5 + letter.count('0') * 3

    ones_list = letter.split('0')
    zeroes_list = letter.split('1')

    for one in ones_list:
        if len(one) > 1:
            current_letter += len(one)

    for zero in zeroes_list:
        if len(zero) > 1:
            current_letter += len(zero)

    message += chr(current_letter)

print(message)
