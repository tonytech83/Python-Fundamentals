sequence = input()

new_sequence = ''

strength = 0

while '>' in sequence:
    if not sequence:
        break

    if sequence[0] == '>':
        new_sequence += '>'
        sequence = sequence[1:]
        strength += int(sequence[0])
        for remove in range(1, strength + 1):
            sequence = sequence[1:]
            strength -= 1
            if not sequence:
                break
            if sequence[0] == '>':
                break

    else:
        char = sequence[:1]
        new_sequence += char
        sequence = sequence[1:]

print(new_sequence + sequence)