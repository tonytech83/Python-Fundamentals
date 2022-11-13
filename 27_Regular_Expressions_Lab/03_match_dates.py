import re

pattern = r'(\d{2})([/.-])([A-Z][a-z]{2})(\2)(\d{4})'
data = input()

matches = re.finditer(pattern, data)

for match in matches:
    print(f'Day: {match.group(1)}, Month: {match.group(3)}, Year: {match.group(5)}')
