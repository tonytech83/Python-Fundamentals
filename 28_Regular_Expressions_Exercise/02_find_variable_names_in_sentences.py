import re

pattern = r'\b_(?P<variable_name>[A-Za-z0-9]+)\b'
data = input()
valid_variables = []
matches = re.finditer(pattern, data, re.MULTILINE)

for match in matches:
    valid_variables.append(match.group('variable_name'))

print(','.join(valid_variables))
