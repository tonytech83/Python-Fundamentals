data = input().split()
search_for = input().split()

products = {}

for idx in range(0, len(data), 2):
    products[data[idx]] = data[idx + 1]

for product in search_for:
    if product in products:
        quantity = products[product]
        print(f'We have {quantity} of {product} left')
    else:
        print(f"Sorry, we don't have {product}")
