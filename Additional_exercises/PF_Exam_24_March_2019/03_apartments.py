import re


def collect_apartments(data):
    global apartments_db
    neighborhood, numbers = data.split(' -> ')
    block_numbers_list_str = numbers.split(',')
    block_numbers_list = list(map(int, block_numbers_list_str))
    if neighborhood not in apartments_db:
        apartments_db[neighborhood] = {}
        for number in block_numbers_list:
            apartments_db[neighborhood][number] = {'apartments': 0, 'price': None}
    else:
        for number in block_numbers_list:
            if not number in apartments_db[neighborhood].keys():
                apartments_db[neighborhood][number] = {'apartments': 0, 'price': None}


def assigning_data(data):
    global apartments_db
    data_1, data_2 = data.split(' -> ')
    pattern = r'([A-Za-z0-9]+)&(\d+)'
    matches = re.findall(pattern, data_1)
    neighborhood = matches[0][0]
    block_number = int(matches[0][1])
    apartments_count, price = data_2.split('|')

    if neighborhood in apartments_db:
        if block_number in apartments_db[neighborhood]:
            apartments_db[neighborhood][block_number]['apartments'] = apartments_count
            apartments_db[neighborhood][block_number]['price'] = price


apartments_db = {}


def output():
    ordered_apartments = sorted(apartments_db.keys())
    for neighborhood in ordered_apartments:
        print(f'Neighborhood: {neighborhood}')
        ordered_block_numbers = sorted(apartments_db[neighborhood].keys())
        for number in ordered_block_numbers:
            print(f"* Block number: {number} -> {apartments_db[neighborhood][number]['apartments']}"
                  f" apartments for sale. Price for one: {apartments_db[neighborhood][number]['price']}")


def main():
    while True:
        research = input()
        if research == 'collectApartments':
            break
        collect_apartments(research)

    while True:
        real_data = input()
        if real_data == 'report':
            output()
            break
        assigning_data(real_data)


main()
