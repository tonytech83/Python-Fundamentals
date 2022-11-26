import re

key_string = input()
text = input()

start_pattern = r'^([A-Za-z]+)[\<\\|\\]'
end_pattern = r'[\<\\|\\]([A-Za-z]+)$'
start = re.search(start_pattern, key_string)[1]
end = re.search(end_pattern, key_string)[1]


pattern = rf'{start}(.*?){end}'
matches = re.findall(pattern, text)
result = ''
result += ''.join(matches)

if result:
    print(result)
else:
    print('Empty result')
