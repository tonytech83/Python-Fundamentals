from collections import deque

sequence_of_integers = []

for number in input().split(' '):
    sequence_of_integers.append(int(number))

average_value = sum(sequence_of_integers) / len(sequence_of_integers)
top_five = deque()

for _ in range(len(sequence_of_integers)):

    number = max(sequence_of_integers)

    if number > average_value:
        top_five.append(max(sequence_of_integers))
        sequence_of_integers.remove(max(sequence_of_integers))

    if len(top_five) == 5:
        break

if len(top_five) == 0:
    print('No')

print(*top_five)
