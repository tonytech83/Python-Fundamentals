items = [x for x in input().split('|')]

budget = float(input())
TICKET_PRICE = 150
CLOTHES_PRICE = 50
SHOES_PRICE = 35
ACCESSORIES_PRICE = 20.50

sell_price = []
profit = 0

for item in items:
    current_item = item.split('->')
    item_type = current_item[0]
    item_price = float(current_item[1])

    if budget < item_price:
        continue

    if (item_type == 'Clothes' and item_price <= CLOTHES_PRICE or
            item_type == 'Shoes' and item_price <= SHOES_PRICE or
            item_type == 'Accessories' and item_price <= ACCESSORIES_PRICE):

        budget -= item_price
        new_price = item_price * 1.4
        sell_price.append(new_price)
        profit += new_price - item_price

for sell in sell_price:
    print(f'{sell:.2f}', end=' ')
print()
print(f'Profit: {profit:.2f}')
if budget + sum(sell_price) >= TICKET_PRICE:
    print('Hello, France!')
else:
    print('Not enough money.')
