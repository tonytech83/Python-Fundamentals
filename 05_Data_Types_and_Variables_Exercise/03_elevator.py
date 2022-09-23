number_of_people = int(input())
elevator_capacity = int(input())

courses = 0

while True:
    courses += 1
    number_of_people -= elevator_capacity

    if number_of_people <= 0:
        break

print(courses)
