import re

pattern = r'(?P<day>\d{2})(?P<separator>[/\.-])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})'
data = input()

valid_dates = re.finditer(pattern, data)

for date in valid_dates:
    current_date = date.groupdict()
    print(f'Day: {current_date["day"]}, Month: {current_date["month"]}, Year: {current_date["year"]}')
