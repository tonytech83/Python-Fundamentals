import re

text = input()
result = ''
pattern = r'\s([A-Za-z0-9]+[\-\.\_]?[A-Za-z0-9]+@[A-Za-z]+[\-\.]?[A-Za-z]+[\-\.]?[A-Za-z]+\.[A-Za-z]+)'
matches = re.findall(pattern, text)

result += '\n'.join(matches)
print(result)