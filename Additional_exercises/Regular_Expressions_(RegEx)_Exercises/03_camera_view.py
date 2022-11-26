import re

skip, take = input().split()
text = input()

pattern = r'\|<(\w+)'
matches = re.findall(pattern, text)

result = []
for match in matches:
    camera = match[int(skip):(int(skip) + int(take))]
    result.append(camera)

print(*result, sep=', ')
