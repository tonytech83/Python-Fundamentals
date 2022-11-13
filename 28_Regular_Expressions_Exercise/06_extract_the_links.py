import re

pattern = r'(?P<url>www\.([A-Za-z0-9]+(\-[A-Za-z0-9]+)*)\.([a-z\.]+[\-a-z]+))'

while True:
    data = input()

    if not data:
        break

    valid_link = re.finditer(pattern, data)

    for url in valid_link:
        print(url.group('url'))
