sequence = input()

new_sequence = [sequence[0]]

for char in sequence:
    if char not in new_sequence[-1]:
        new_sequence.append(char)

print(*new_sequence, sep='')
