people_waiting = int(input())
lift_wagons = []

for wagon in input().split(' '):
    lift_wagons.append(int(wagon))

for wagon in range(len(lift_wagons)):

    if people_waiting == 0:
        break

    for person in range(4):

        if lift_wagons[wagon] == 4:
            break

        lift_wagons[wagon] += 1
        people_waiting -= 1

        if people_waiting == 0:
            break

if people_waiting > 0:
    print(f'There isn\'t enough space! {people_waiting} people in a queue!')

if people_waiting == 0:
    pass

if lift_wagons[-1] < 4:
    print('The lift has empty spots!')

print(*lift_wagons, sep=' ')
