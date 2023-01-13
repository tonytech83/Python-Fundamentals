"""
Please don't laugh at me too much, this is my first attempt to solve this type of task :)
There is many work to do here but no time for this right now
"""

def read_maze():
    """
    This func read maze and player coordinates
    :return: maze, player coordinates
    """
    rows = int(input())
    received_maze = []
    row = 0
    col = 0
    for row_idx in range(rows):
        current_row = input()
        for col_idx in range(len(current_row)):
            if current_row[col_idx] == 'k':
                row = row_idx
                col = col_idx
        received_maze.append([x for x in current_row])

    return received_maze, row, col


def is_outside(row, col):
    """
    This func checks whether we are out of the maze or not
    """
    return row not in range(len(maze)) or col not in range(len(maze[0]))


def way_finder(row, col, maze, path, attempt):
    """
    Recursive func finding path in maze
    """
    global player_out

    if attempt == 'right':
        directions = [
            (row, col + 1),  # right
            (row + 1, col),  # down
            (row, col - 1),  # left
            (row - 1, col),  # up
        ]
    elif attempt == 'down':
        directions = [
            (row + 1, col),  # down
            (row, col - 1),  # left
            (row - 1, col),  # up
            (row, col + 1),  # right
        ]
    elif attempt == 'left':
        directions = [
            (row, col - 1),  # left
            (row - 1, col),  # up
            (row, col + 1),  # right
            (row + 1, col),  # down
        ]
    else:
        directions = [
            (row - 1, col),  # up
            (row, col + 1),  # right
            (row + 1, col),  # down
            (row, col - 1),  # left
        ]

    for row_idx, col_idx in directions:
        if is_outside(row_idx, col_idx):
            player_out = True
            return player_out
        if maze[row_idx][col_idx] == FREE_CELL:
            maze[row][col] = WALL
            path.append([row_idx, col_idx])
            return way_finder(row_idx, col_idx, maze, path, attempt)
        elif maze[row_idx][col_idx] == WALL:
            continue


maze, player_row, player_col = read_maze()

DIRECTIONS = ['right', 'down', 'left', 'up']
FREE_CELL = ' '
WALL = '#'

max_path = 0
player_out = False

for attempt in DIRECTIONS:
    path = []
    player_out = way_finder(player_row, player_col, maze, path, attempt)
    current_path = 1 + len(path)

    # searching for longest path if player is outside of maze
    if player_out and current_path > max_path:
        max_path = current_path

if max_path > 0:
    print(f'Kate got out in {max_path} moves')
else:
    print('Kate cannot get out')
