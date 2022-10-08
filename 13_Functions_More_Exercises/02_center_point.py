import math


def point_closest_to_center(coordinates):
    distances = []
    for point in coordinates:
        current_distance = math.sqrt(pow(point[0], 2) + pow(point[-1], 2))
        distances.append(current_distance)
    return distances.index(min(distances))


coordinates = []
for _ in range(2):
    current_coordinates = []
    for _ in range(2):
        digit = math.floor(float(input()))
        current_coordinates.append(digit)
    coordinates.append(current_coordinates)

min_distance = point_closest_to_center(coordinates)
closest_to_center = coordinates[min_distance]
print(f'({closest_to_center[0]}, {closest_to_center[1]})')
