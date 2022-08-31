decorations_count = int(input())
days = int(input())

ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15

price = 0
christmas_points = 0

additional_point = False

for day in range(1, days + 1):

    if day % 11 == 0:
        decorations_count += 2

    if day % 2 == 0:
        price += decorations_count * ornament_set
        christmas_points += 5

    if day % 3 == 0:
        price += decorations_count * (tree_skirt + tree_garlands)
        christmas_points += 13
        additional_point = True

    if day % 5 == 0:
        price += decorations_count * tree_lights
        christmas_points += 17
        if additional_point:
            christmas_points += 30

    additional_point = False

    if day % 10 == 0:
        price += tree_skirt + tree_garlands + tree_lights
        christmas_points -= 20
        if day == days:
            christmas_points -= 30

print(f'Total cost: {price}')
print(f'Total spirit: {christmas_points}')
