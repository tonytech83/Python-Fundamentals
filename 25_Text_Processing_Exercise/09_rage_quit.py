string = input().upper()

non_numerical = ''
symbols = []
result = ''
idx = 0

while idx < len(string):
    number = ''
    if not string[idx].isdigit():
        non_numerical += string[idx]

        if string[idx] not in symbols:
            symbols.append(string[idx])
        idx += 1

    else:
        number += string[idx]
        if idx == len(string) - 1:
            result += non_numerical * int(number)
            non_numerical = ''
            break
        if string[idx + 1].isdigit():
            number += string[idx + 1]
            idx += 1

        result += non_numerical * int(number)
        non_numerical = ''
        idx += 1

print(f'Unique symbols used: {len(symbols)}')
print(result)
