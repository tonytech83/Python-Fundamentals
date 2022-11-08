strings = input().split()

result = 0

for string in strings:
    number = int(''.join([x for x in string if x.isdigit()]))
    string_result = 0

    if string[0].isupper():
        first_letter = ord(string[0]) - 64
        string_result += number / first_letter
    else:
        first_letter = ord(string[0]) - 96
        string_result += number * first_letter

    if string[-1].isupper():
        last_letter = ord(string[-1]) - 64
        string_result = string_result - last_letter
    else:
        last_letter = ord(string[-1]) - 96
        string_result = string_result + last_letter

    result += string_result

print(f'{result:.2f}')
