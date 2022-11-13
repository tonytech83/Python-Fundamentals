import re

pattern = r'(?P<number>\d+)'

while True:
    line = input()
    if not line:
        break
    numbers = re.finditer(pattern, line, re.MULTILINE)
    for number in numbers:
        print(number.group('number'), end=' ')
