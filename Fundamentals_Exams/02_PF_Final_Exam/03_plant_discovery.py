def read_input(lines_to_read):
    """
    This function reads input from console and store the information in plants_info dict.
    :param lines_to_read: int
    """
    global plants_info
    for _ in range(lines_to_read):
        new_plant, rarity = input().split('<->')
        if new_plant not in plants_info:
            plants_info[new_plant] = {}
            plants_info[new_plant]['Rarity'] = rarity
            plants_info[new_plant]['Rating'] = [0]
        else:
            plants_info[new_plant]['Rarity'] = rarity


def plant_rate(current_data):
    """
    This function add the given rating to the plant if it exists else print 'error'
    :param current_data: str
    """
    global plants_info
    plant_to_rate, rating = current_data.split(' - ')
    if plant_to_rate in plants_info:
        plants_info[plant_to_rate]['Rating'].append(int(rating))
    else:
        print('error')


def plant_update(current_data):
    """
    This function update the rarity of the plant with the new one
    :param current_data: str
    """
    global plants_info
    plant_to_update, new_rarity = current_data.split(' - ')
    if plant_to_update in plants_info:
        plants_info[plant_to_update]['Rarity'] = int(new_rarity)
    else:
        print('error')


def plant_reset(current_data):
    """
    This function remove all the ratings of the given plant
    :param current_data: str
    """
    global plants_info
    plant_to_reset = current_data
    if plant_to_reset in plants_info:
        plants_info[plant_to_reset]['Rating'] = [0]
    else:
        print('error')


def output():
    """
    This function prints data stored in plants_info
    """
    global plants_info
    print('Plants for the exhibition:')
    for plant, info in plants_info.items():
        plant_rarity = info['Rarity']
        plant_rating = sum(info['Rating'])
        if len(info['Rating']) > 1:
            plant_rating = sum(info['Rating']) / (len(info['Rating']) - 1)
        print(f'- {plant}; Rarity: {plant_rarity}; Rating: {plant_rating:.2f}')


plants_info = {}
lines = int(input())

read_input(lines)

while True:
    command = input()
    if command == 'Exhibition':
        break

    event, data = command.split(':')

    if event == 'Rate':
        plant_rate(data.strip())
    elif event == 'Update':
        plant_update(data.strip())
    elif event == 'Reset':
        plant_reset(data.strip())

output()
