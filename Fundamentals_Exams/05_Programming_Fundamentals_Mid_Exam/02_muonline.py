rooms = input().split('|')

max_health = 100
health = max_health
bitcoins = 0
best_room = 0
killed = False

for room in rooms:
    current_room = room.split(' ')
    event = current_room[0]
    number = int(current_room[1])

    best_room += 1

    if event == 'potion':
        if health + number > max_health:
            healed_by = max_health - health
            health = max_health
        else:
            healed_by = number
            health += healed_by
        print(f'You healed for {healed_by} hp.')
        print(f'Current health: {health} hp.')

    elif event == 'chest':
        bitcoins += number
        print(f'You found {number} bitcoins.')

    else:
        health -= number
        if health > 0:
            print(f'You slayed {event}.')
        else:
            print(f'You died! Killed by {event}.')
            killed = True
            break

if not killed:
    print(f'You\'ve made it!\nBitcoins: {bitcoins}\nHealth: {health}')
else:
    print(f'Best room: {best_room}')
