from collections import deque


def read_matrix():
    """
    Read matrix from console
    :return: Returns matrix and coordinates of all dots in matrix
    """
    current_matrix = []
    dots_coord = deque()
    rows = int(input())
    for row in range(rows):
        current_row = input().split()
        for col in range(len(current_row)):
            if current_row[col] == '.':
                dots_coord.append((row, col))
        current_matrix.append(current_row)

    return current_matrix, dots_coord


def is_inside(row, col):
    """
    Checks coordinates are in matrix
    :param row: row of next move
    :param col: col of next move
    :return: boolean
    """
    return row in range(len(matrix)) and col in range(len(matrix[0]))


def dot_count_finder(row, col, count):
    """
    Recursive function with found the longest path form starting point.
    :param row: row of starting point
    :param col: col of starting point
    :param count: set of all unique points in matrix which can be connected from starting point.
    :return: set of unique points
    """
    global matrix

    directions = [
        [row, col + 1],  # left
        [row + 1, col],  # down
        [row, col - 1],  # right
        [row - 1, col],  # up
    ]

    for next_row, next_col in directions:
        if is_inside(next_row, next_col):
            if matrix[next_row][next_col] == '.':
                matrix[row][col] = '-'
                count.add((next_row, next_col))
                dot_count_finder(next_row, next_col, count)
            else:
                continue
        else:
            continue

    return count


matrix, dots_coordinates = read_matrix()

max_dots_count = 0

while dots_coordinates:
    # takes first point coordinates and add them to dots set
    point_row, point_col = dots_coordinates.popleft()
    dots = {(point_row, point_col)}

    dots_count = dot_count_finder(point_row, point_col, dots)

    current_dots_count = len(dots.union(dots_count))

    if current_dots_count > max_dots_count:
        max_dots_count = current_dots_count

print(max_dots_count)
