import math


def line_len(line):
    line_length = math.sqrt(pow((line[2] - line[0]), 2) + pow((line[3] - line[1]), 2))
    return line_length


def point_closest_to_center(point):
    distance_to_center = math.sqrt(pow(point[0], 2) + pow(point[1], 2))
    return distance_to_center


point_1 = [math.floor(float(input())), math.floor(float(input()))]
point_2 = [math.floor(float(input())), math.floor(float(input()))]
point_3 = [math.floor(float(input())), math.floor(float(input()))]
point_4 = [math.floor(float(input())), math.floor(float(input()))]
line_one = point_1 + point_2
line_two = point_3 + point_4
line_one_len = line_len(line_one)
line_two_len = line_len(line_two)

if line_one_len > line_two_len:
    dist_1 = point_closest_to_center(point_1)
    dist_2 = point_closest_to_center(point_2)
    if dist_1 <= dist_2:
        line = point_1 + point_2
    else:
        line = point_2 + point_1
else:
    dist_1 = point_closest_to_center(point_3)
    dist_2 = point_closest_to_center(point_4)
    if dist_1 <= dist_2:
        line = point_3 + point_4
    else:
        line = point_4 + point_3

print(f'({line[0]}, {line[1]})({line[2]}, {line[3]})')
