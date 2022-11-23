def seek_through_dungeon(rooms, health, best_room, died):
    current_health = health
    bitcoins = 0

    for room in rooms:
        if current_health <= 0:
            break

        best_room += 1
        event, value = room.split()

        if event == 'potion':
            if current_health + int(value) > 100:
                healed_with = 100 - current_health
                current_health = 100
            else:
                healed_with = int(value)
                current_health += healed_with
            print(f'You healed for {healed_with} hp.')
            print(f'Current health: {current_health} hp.')

        elif event == 'chest':
            bitcoins += int(value)
            print(f'You found {value} bitcoins.')

        else:
            current_health -= int(value)
            if current_health > 0:
                print(f'You slayed {event}.')
            else:
                died = True
                print(f'You died! Killed by {event}.')
                print(f'Best room: {best_room}')

    return bitcoins, current_health, best_room, died


dungeon = [x for x in input().split('|')]
max_health = 100
visited_rooms = 0
killed = False

btc, health, best_room, killed = seek_through_dungeon(dungeon, max_health, visited_rooms, killed)
if not killed:
    print(f"You've made it!\nBitcoins: {btc}\nHealth: {health}")
