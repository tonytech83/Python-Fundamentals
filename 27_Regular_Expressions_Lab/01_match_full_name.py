import re

sequence = input()

pattern = r'\b[A-Z][a-z]+\b \b[A-Z][a-z]+\b'

full_names = re.findall(pattern, sequence)

for full_name in full_names:
    print(full_name, end=' ')
