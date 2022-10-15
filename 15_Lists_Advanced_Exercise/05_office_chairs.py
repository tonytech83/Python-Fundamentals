def check_chairs(business_center):
    free_chairs = []
    for room in business_center:
        current_room = room.split()
        chairs = len(current_room[0])
        persons = int(current_room[1])
        free_chairs.append(chairs - persons)

    if sum(free_chairs) >= 0:
        return print(f'Game On, {sum(free_chairs)} free chairs left')

    for idx in range(len(free_chairs)):
        if free_chairs[idx] < 0:
            print(f'{abs(free_chairs[idx])} more chairs needed in room {idx + 1}')


def main():
    number_of_rooms = int(input())
    rooms = []
    for _ in range(number_of_rooms):
        current_room = input()
        rooms.append(current_room)

    check_chairs(rooms)


main()
