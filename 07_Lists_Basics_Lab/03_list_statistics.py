lines = int(input())

number_list = []

positives = []
negatives = []

for _ in range(lines):
    current_number = int(input())
    number_list.append(current_number)

for number in number_list:
    if number >= 0:
        positives.append(number)
    else:
        negatives.append(number)

print(positives)
print(negatives)
print(f'Count of positives: {len(positives)}')
print(f'Sum of negatives: {sum(negatives)}')
