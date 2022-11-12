import math

budget = float(input())
students = int(input())
package_flour_price = float(input())
single_egg_price = float(input())
single_apron_price = float(input())

free_package_flour = students // 5

total_flour_price = package_flour_price * (students - free_package_flour)
total_eggs_price = single_egg_price * 10 * students
total_apron_price = single_apron_price * math.ceil(students * 1.2)

total_price = total_flour_price + total_eggs_price + total_apron_price

if total_price <= budget:
    print(f'Items purchased for {total_price:.2f}$.')
else:
    diff = abs(budget - total_price)
    print(f'{diff:.2f}$ more needed.')
