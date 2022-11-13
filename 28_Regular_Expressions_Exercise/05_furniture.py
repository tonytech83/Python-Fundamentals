import re

pattern = r'^>>(?P<item>([A-Za-z]+))<<(?P<price>(\d+\.?\d*))!(?P<quantity>(\d+))$'
valid_items = []
total_spend = 0

while True:
    purchase_info = input()

    if purchase_info == 'Purchase':
        break

    valid_info = re.match(pattern, purchase_info)
    if valid_info is not None:
        furniture_name = valid_info.group('item')
        price = valid_info.group('price')
        quantity = valid_info.group('quantity')

        valid_items.append(furniture_name)
        total_spend += float(price) * int(quantity)

print('Bought furniture:')
for furniture in valid_items:
    print(furniture)
print(f'Total money spend: {total_spend:.2f}')
