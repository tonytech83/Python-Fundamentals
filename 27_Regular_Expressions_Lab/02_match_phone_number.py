import re

pattern = r'(\+359 2 \d{3} \d{4}\b)|(\+359-2-\d{3}-\d{4}\b)'
data = input()

matches = re.finditer(pattern, data)
valid_phone_numbers = [match.group() for match in matches]
print(*valid_phone_numbers, sep=', ')
