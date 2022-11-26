number = int(input())

for row in range(1, number + 1):
    print('*' * row)

for row in range(number - 1, 0, -1):
    print('*' * row)
