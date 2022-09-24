snowballs_number = int(input())

best_value = 0
best_weight = 0
best_time = 0
best_quality = 0

for snowball in range(snowballs_number):
    snowball_weight = int(input())
    needed_time = int(input())
    quality = int(input())

    snowball_value = (snowball_weight / needed_time) ** quality

    if best_value <= snowball_value:
        best_value = snowball_value
        best_weight = snowball_weight
        best_time = needed_time
        best_quality = quality

print(f'{best_weight} : {best_time} = {int(best_value)} ({best_quality})')
