single_string = input()

digits = []
letters = []
others = []

for char in single_string:
    if char.isdigit():
        digits.append(char)
    elif char.isalpha():
        letters.append(char)
    else:
        others.append(char)

print(*digits, sep='')
print(*letters, sep='')
print(*others, sep='')
