def valid_contest(all_contests, contest):
    """
    Check if contest is in initial inputs of contests
    """
    if contest in all_contests:
        return True
    return False


def valid_password(all_contests, contest, password):
    """
    Check if provided password from student is valid
    """
    if all_contests[contest] == password:
        return True
    return False


def init_user(contest_results, contest, username, points, total_points):
    """
    If the contest and the password are valid, save the user with the contest they take part in
    (a user can take part in many contests) and the points the user has in the given contest.
    If you receive the same contest and the same user
    update the points only if the new ones are more than the older ones.
    """
    if contest not in contest_results:
        contest_results[contest] = {}
        contest_results[contest][username] = points
        if username not in total_points:
            total_points[username] = points
        else:
            total_points[username] += points
    else:
        if username in contest_results[contest].keys():
            if contest_results[contest][username] < points:
                diff_points = points - contest_results[contest][username]
                contest_results[contest][username] = points
                total_points[username] += diff_points
        else:
            contest_results[contest][username] = points
            if username not in total_points:
                total_points[username] = points
            else:
                total_points[username] += points


all_contests = {}

while True:
    line = input()
    if line == 'end of contests':
        break
    contest, password = line.split(':')
    all_contests[contest] = password

contest_results = {}
# create new dict to store total points for each student
user_total_points = {}

while True:
    line = input()
    if line == 'end of submissions':
        break
    data = line.split('=>')
    contest = data[0]
    password = data[1]
    username = data[2]
    points = int(data[3])
    if valid_contest(all_contests, contest) and valid_password(all_contests, contest, password):
        init_user(contest_results, contest, username, points, user_total_points)

# find the best student by points
sorted_dict = dict(sorted(user_total_points.items(), key=lambda kvp: -kvp[1]))
winner = list(sorted_dict.items())[:1]
print(f'Best candidate is {winner[0][0]} with total {winner[0][1]} points.')
# ranking
print('Ranking:')
# print students ordered by their names
for user in sorted(user_total_points.items(), key=lambda kvp: kvp[0]):
    current_user = user[0]
    print(current_user)
    # create dict for each student with structure {contest: points}
    current_user_contests = {}
    for contest, user_data in contest_results.items():
        if current_user in user_data:
            current_user_contests[contest] = user_data[user[0]]
    # For each user print each contest with the points in descending order.
    for current_contest, current_points in sorted(current_user_contests.items(), key=lambda kvp: -kvp[1]):
        print(f'#  {current_contest} -> {current_points}')
