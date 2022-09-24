pour_times = int(input())

tank_capacity = 255
water_in_tank = 0

for pour in range(pour_times):
    litters_pour = int(input())
    if tank_capacity < litters_pour:
        print('Insufficient capacity!')
        continue
    else:
        tank_capacity -= litters_pour
        water_in_tank += litters_pour

print(water_in_tank)
