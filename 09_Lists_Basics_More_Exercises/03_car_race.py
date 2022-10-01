race_track = [int(x) for x in input().split()]

half_track = len(race_track) // 2

left_total_time = 0
right_total_time = 0

for step in range(1, half_track + 1):
    left_car = step - 1
    right_car = -step

    if race_track[left_car] == 0:
        left_total_time *= 0.8
    else:
        left_total_time += race_track[left_car]
    if race_track[right_car] == 0:
        right_total_time *= 0.8
    else:
        right_total_time += race_track[right_car]

if left_total_time < right_total_time:
    total_time = left_total_time
    winner = 'left'
else:
    total_time = right_total_time
    winner = 'right'

print(f'The winner is {winner} with total time: {total_time:.1f}')
