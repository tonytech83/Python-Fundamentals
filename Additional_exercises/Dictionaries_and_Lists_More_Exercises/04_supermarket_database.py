database = {}

while True:
    # received information from console
    command = input()

    # when received command == 'stocked' break the cycle
    if command == 'stocked':
        break

    # split the information from input to three variables
    product, price, quantity = command.split()

    # check the existence of product in database
    if product not in database:
        database[product] = [float(price), int(quantity)]
    else:
        database[product][0] = float(price)
        database[product][1] += int(quantity)

grand_total = 0

# iterating through database and print information about all of products
for product, info in database.items():
    total = info[0] * info[1]
    grand_total += total
    print(f'{product}: ${info[0]:.2f} * {info[1]} = ${total:.2f}')

# print the total price of all products
print('-' * 30)
print(f'Grand Total: ${grand_total:.2f}')
