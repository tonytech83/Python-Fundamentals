food_quantity = float(input()) * 1000
hay_quantity = float(input()) * 1000
cover_quantity = float(input()) * 1000
pig_weight = float(input()) * 1000

month = 30
is_enough = False

for day in range(1, month + 1):

    food_quantity -= 300

    # check if run out of food, hay or cover
    if food_quantity <= 0 or hay_quantity <= 0 or cover_quantity <= 0:
        is_enough = True
        break

    if day % 2 == 0:
        hay_quantity -= food_quantity * 0.05

    if day % 3 == 0:
        cover_quantity -= pig_weight / 3

if is_enough:
    print('Merry must go to the pet store!')
else:
    print(f'Everything is fine! Puppy is happy! Food: {(food_quantity / 1000):.2f},'
          f' Hay: {(hay_quantity / 1000):.2f}, Cover: {(cover_quantity / 1000):.2f}.')
