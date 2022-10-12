def calc_total_price(quantity, prices):
    price = 0

    for item in prices:
        current_item = item[0]
        if current_item == chosen_product:
            price = item[1]
    return price * quantity


prices = [['coffee', 1.50], ['water', 1.00], ['coke', 1.40], ['snacks', 2.00]]

chosen_product = input()
quantity = int(input())

print(f'{calc_total_price(quantity, prices):.2f}')
