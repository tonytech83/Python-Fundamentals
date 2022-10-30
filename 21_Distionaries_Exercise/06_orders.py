def total_price_by_items(all_items):
    for key, value in all_items.items():
        print(f'{key} -> {(value[0] * value[1]):.2f}')


market = {}

while True:
    line = input()
    if line == 'buy':
        break

    product, price, qty = line.split()
    if product not in market:
        market[product] = []
        market[product].append(float(price))
        market[product].append(int(qty))
    else:
        market[product][0] = float(price)
        market[product][1] += int(qty)

total_price_by_items(market)
