import re

sequence = input()

pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'

valid_names = re.findall(pattern, sequence)

print(*valid_names)
