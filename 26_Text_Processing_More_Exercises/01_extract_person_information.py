number_of_lines = int(input())

for line in range(number_of_lines):
    name = ''
    data = [x for x in input()]
    idx_of_at = data.index('@')
    idx_of_pipe = data.index('|')
    for char in range(idx_of_at + 1, idx_of_pipe):
        name += data[char]

    age = ''
    idx_of_hash = data.index('#')
    idx_of_asterix = data.index('*')
    for digit in range(idx_of_hash + 1, idx_of_asterix):
        age += data[digit]

    print(f'{name} is {age} years old.')
