import re

sequence = input()
word = input()

pattern = rf'\b{word}\b'

matches = re.findall(pattern, sequence, re.IGNORECASE)

print(len(matches))
