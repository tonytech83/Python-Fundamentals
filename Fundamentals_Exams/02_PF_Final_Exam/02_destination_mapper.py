import re

places = input()

pattern = r'(?P<sep>[=|\/])(?P<place>[A-Z][A-Za-z]{2,})(?P=sep)'
matches = re.finditer(pattern, places)

matched_places = []
travel_points = 0

for match in matches:
    matched_places.append(match.group('place'))
    travel_points += len(match.group('place'))

print(f'Destinations: {", ".join(matched_places)}')
print(f'Travel Points: {travel_points}')
