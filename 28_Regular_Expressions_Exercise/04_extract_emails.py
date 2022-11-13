import re

pattern = r'(?P<username>(?<=\s)[a-zA-Z0-9]+[a-zA-Z0-9\.\-\_]*)\@(?P<domain>[a-zA-Z]+[a-zA-Z\-\.]*\.[a-zA-Z]+)'
line = input()

valid_emails = re.finditer(pattern, line)

for email in valid_emails:
    print(f'{email.group("username")}@{email.group("domain")}')
