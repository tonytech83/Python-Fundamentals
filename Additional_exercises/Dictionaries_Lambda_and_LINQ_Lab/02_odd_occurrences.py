sequence = {}

for element in input().split():
    if element.lower() not in sequence:
        sequence[element.lower()] = 0
    sequence[element.lower()] += 1

odd_occurrences = []

for key, value in sequence.items():
    if value % 2 != 0:
        odd_occurrences.append(key)

print(*odd_occurrences, sep=', ')