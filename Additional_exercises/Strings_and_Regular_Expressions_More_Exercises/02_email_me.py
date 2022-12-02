import re

email_address = input()

pattern = r'(?P<before>.*)@(?P<after>.*)'
matches = re.search(pattern, email_address)

before_sum = 0
for char in matches['before']:
    before_sum += ord(char)

after_sum = 0
for char in matches['after']:
    after_sum += ord(char)

total = before_sum - after_sum

if total >= 0:
    print('Call her!')
else:
    print('She is not the one.')
