budget = int(input())

product_price = input()

while product_price != "End":
    budget -= int(product_price)
    if budget < 0:
        print('You went in overdraft!')
        break

    product_price = input()

else:
    print('You bought everything needed.')
