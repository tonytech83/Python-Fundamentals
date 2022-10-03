price = input()
customer_type = ['special', 'regular']

price_without_taxes = 0
taxes = 0
total_price = 0

while price not in customer_type:
    if float(price) < 0:
        print('Invalid price!')
        price = input()
        continue

    price_without_taxes += float(price)
    taxes += float(price) * 0.2

    price = input()

total_price = price_without_taxes + taxes

if total_price == 0:
    print('Invalid order!')
else:
    if price == 'special':
        total_price *= 0.9

    print(f'Congratulations you\'ve just bought a new computer!')
    print(f'Price without taxes: {price_without_taxes:.2f}$')
    print(f'Taxes: {taxes:.2f}$')
    print('-----------')
    print(f'Total price: {total_price:.2f}$')
