cells = [x for x in input().split('#')]

watter_amount = int(input())

high = range(81, 126)
medium = range(51, 81)
low = range(1, 51)

effort = 0
total_fire = 0
valid_cells = []

for data in cells:
    current_cell = data.split(' = ')
    type_of_fire = current_cell[0]
    power_of_fire = int(current_cell[1])

    if watter_amount < power_of_fire:
        continue

    if (type_of_fire == 'High' and power_of_fire in high or
            type_of_fire == 'Medium' and power_of_fire in medium or
            type_of_fire == 'Low' and power_of_fire in low):
        watter_amount -= power_of_fire
        total_fire += power_of_fire
        effort += power_of_fire * 0.25
        valid_cells.append(power_of_fire)

    if watter_amount <= 0:
        break

print('Cells:')
for fire in valid_cells:
    print(f' - {fire}')

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
