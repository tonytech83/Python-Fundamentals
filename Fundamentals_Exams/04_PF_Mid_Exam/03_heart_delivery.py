def all_equal(neighborhood):
    return not neighborhood or neighborhood.count(neighborhood[0]) == len(neighborhood)


neighborhood = []

for house in input().split('@'):
    neighborhood.append(int(house))

house_idx = 0
command = [None]

while True:

    for house in neighborhood:

        command = input().split(' ')

        if command[0] == 'Love!':
            break

        length_of_jump = int(command[1])
        house_idx += length_of_jump
        if house_idx >= len(neighborhood):
            house_idx = 0
            current_house = neighborhood[house_idx]
        else:
            current_house = neighborhood[house_idx]

        if current_house == 0:
            print(f'Place {house_idx} already had Valentine\'s day.')
            continue
        else:
            neighborhood[house_idx] -= 2

        if neighborhood[house_idx] == 0:
            print(f'Place {house_idx} has Valentine\'s day.')

    if command[0] == 'Love!':
        break

print(f'Cupid\'s last position was {house_idx}.')

if all_equal(neighborhood):
    print('Mission was successful.')
else:
    success = neighborhood.count(0)
    fails = len(neighborhood) - success
    print(f'Cupid has failed {fails} places.')
