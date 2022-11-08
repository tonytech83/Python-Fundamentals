def first_letter_check(first_letter, current_result):
    if first_letter.isupper():
        first_letter = ord(string[0]) - 64
        current_result += number / first_letter
    else:
        first_letter = ord(string[0]) - 96
        current_result += number * first_letter
    return current_result


def last_letter_check(last_letter, current_result):
    if last_letter.isupper():
        last_letter = ord(string[-1]) - 64
        current_result -= last_letter
    else:
        last_letter = ord(string[-1]) - 96
        current_result += last_letter
    return current_result


strings = input().split()

result = 0

for string in strings:
    number = int(''.join([x for x in string if x.isdigit()]))
    string_result = 0

    intermediate_result = first_letter_check(string[0], string_result)
    string_result = last_letter_check(string[-1], intermediate_result)
    result += string_result

print(f'{result:.2f}')
