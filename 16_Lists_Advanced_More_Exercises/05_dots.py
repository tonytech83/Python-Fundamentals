def largest_count_dots(row, col, matrix, dot_counter):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return
    if matrix[row][col] == '-':
        return
    if matrix[row][col] == '.':
        dot_counter += 1


rows = int(input())

matrix = []

for _ in range(rows):
    matrix.append([x for x in input().split()])

counter = 0

largest_count_dots(0, 0, matrix, counter)

# TODO
