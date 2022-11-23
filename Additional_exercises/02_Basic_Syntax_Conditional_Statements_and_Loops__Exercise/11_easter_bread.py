budget = float(input())
flour_price = float(input())

eggs_price = flour_price * 0.75
milk_price = flour_price * 1.25 / 4
loaf_price = flour_price + eggs_price + milk_price

colored_eggs = 0
loaves_count = 0

while True:

    if budget <= loaf_price:
        break

    colored_eggs += 3
    loaves_count += 1
    budget -= loaf_price

    if loaves_count % 3 == 0:
        colored_eggs -= (loaves_count - 2)

print(f'You made {loaves_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')
