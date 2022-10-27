line = input().split()

products = {}

for idx in range(0, len(line), 2):
    products[line[idx]] = int(line[idx + 1])

print(products)
