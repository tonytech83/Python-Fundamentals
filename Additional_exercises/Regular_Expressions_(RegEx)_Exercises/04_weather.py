import re

weather_forecast = {}

while True:
    data = input()
    if data == 'end':
        break

    pattern = r'([A-Z]{2})(\d{1,2}.\d{1,2})([A-Za-z]+)\|'
    match = re.search(pattern, data)

    if match:
        city = match.group(1)
        temperature = float(match.group(2))
        weather_type = match.group(3)
        weather_forecast[city] = [temperature, weather_type]

for key, value in sorted(weather_forecast.items(), key=lambda kvp: kvp[1][0]):
    print(f'{key} => {value[0]:.2f} => {value[1]}')
