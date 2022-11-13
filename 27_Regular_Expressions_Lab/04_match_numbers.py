import re

pattern = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'
data = input()

matches = re.finditer(pattern, data)

for match in matches:
    print(match.group(), end=' ')
