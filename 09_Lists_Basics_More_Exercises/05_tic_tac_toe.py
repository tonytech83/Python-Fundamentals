row_1 = [int(x) for x in input().split()]
row_2 = [int(x) for x in input().split()]
row_3 = [int(x) for x in input().split()]

player_one_win = False
player_two_win = False

# check if one of the rows contains only "1"
if row_1.count(1) == 3 or row_2.count(1) == 3 or row_3.count(1) == 3:
    player_one_win = True

# check if one of the rows contains only "2"
elif row_1.count(2) == 3 or row_2.count(2) == 3 or row_3.count(2) == 3:
    player_two_win = True

# check if one of the columns contains only "1"
elif (row_1[0] == 1 and row_2[0] == 1 and row_3[0] == 1) or\
        (row_1[1] == 1 and row_2[1] == 1 and row_3[1] == 1) or\
        (row_1[2] == 1 and row_2[2] == 1 and row_3[2] == 1):
    player_one_win = True

# check if one of the columns contains only "2"
elif (row_1[0] == 2 and row_2[0] == 2 and row_3[0] == 2) or\
        (row_1[1] == 2 and row_2[1] == 2 and row_3[1] == 2) or\
        (row_1[2] == 2 and row_2[2] == 2 and row_3[2] == 2):
    player_two_win = True

# if element in middle of row_2 is "1" than check left and right diagonals for "1"
elif row_2[1] == 1:
    if row_1[0] == 1 and row_3[2] == 1 or row_1[2] == 1 and row_3[0] == 1:
        player_one_win = True

# if element in middle of row_2 is "2" than check left and right diagonals for "2"
elif row_2[1] == 2:
    if row_1[0] == 2 and row_3[2] == 2 or row_1[2] == 2 and row_3[0] == 2:
        player_two_win = True

if player_one_win:
    print('First player won')
elif player_two_win:
    print('Second player won')
else:
    print('Draw!')
