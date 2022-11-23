numbers = [int(x) for x in input().split()]

max_equal_elements = 0
max_element = ''

for num in numbers:
    if numbers.count(num) > max_equal_elements:
        max_equal_elements = numbers.count(num)
        max_element = str(num)

print(f'{max_element} ' * max_equal_elements)
