import re

number_of_lines = int(input())

for line in range(number_of_lines):
    data = input()
    name = re.findall(r'@([A-Za-z]\w*)\b', data)
    age = re.findall(r'#(\d*)\b', data)
    if name and age:
        print(f'{name[0]} is {age[0]} years old.')
