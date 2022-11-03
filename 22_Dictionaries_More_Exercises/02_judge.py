def users_total_points(total_points, points, name):
    """
    Calculate the total points given user
    """
    if name not in total_points:
        total_points[name] = int(points)
    else:
        total_points[name] += int(points)


def main(contests, total_points, data):
    """
    Manipulating both dictionaries with data from input
    """
    name, contest, points = data.split(' -> ')
    if contest not in contests:
        contests[contest] = {}
        contests[contest][name] = int(points)
        users_total_points(total_points, points, name)
    else:
        if name not in contests[contest]:
            contests[contest][name] = int(points)
            users_total_points(total_points, points, name)
        else:
            if contests[contest][name] < int(points):
                diff = int(points) - contests[contest][name]
                contests[contest][name] += diff
                users_total_points(total_points, diff, name)


def result(contests, user_total_points):
    """
    Print the results
    """
    for contest in contests:
        print(f'{contest}: {len(contests[contest])} participants')
        participant = 1
        for name, points in sorted(contests[contest].items(), key=lambda kvp: (-kvp[1], kvp[0])):
            print(f'{participant}. {name} <::> {points}')
            participant += 1
    print(f'Individual standings:')
    participant = 1
    for name, points in sorted(user_total_points.items(), key=lambda kvp: (-kvp[1], kvp[0])):
        print(f'{participant}. {name} -> {points}')
        participant += 1


contests = {}
user_total_points = {}

while True:
    line = input()
    if line == 'no more time':
        break

    main(contests, user_total_points, line)

result(contests, user_total_points)
