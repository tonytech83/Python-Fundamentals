orders_count = int(input())

total = 0

for order in range(orders_count):

    price = 0

    capsule_price = float(input()) * 100
    days = int(input())
    capsule_per_day = int(input())

    if 1 <= capsule_price <= 10000.00 and 1 <= days <= 31 and 1 <= capsule_per_day <= 2000:
        price = capsule_price * capsule_per_day * days / 100
        total += price
        print(f'The price for the coffee is: ${price:.2f}')

print(f'Total: ${total:.2f}')

