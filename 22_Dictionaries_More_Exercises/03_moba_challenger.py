def add_points(players_total_points, player_name, player_skill):
    if player_name not in players_total_points:
        players_total_points[player_name] = 0
    players_total_points[player_name] += player_skill


def init_player(players_data, data):
    name = data[0]
    position = data[1]
    skill = int(data[2])
    if name not in players_data:
        players_data[name] = {}
        players_data[name][position] = skill
        add_points(players_total_points, name, skill)
    else:
        if position not in players_data[name]:
            players_data[name][position] = skill
            add_points(players_total_points, name, skill)
        else:
            if players_data[name][position] < skill:
                players_data[name][position] = skill
                diff_points = skill - players_data[name][position]
                add_points(players_total_points, name, diff_points)


def players_exist(players_data, p_one, p_two):
    if p_one in players_data and p_two in players_data:
        return True
    return False


def common_position(players_data, p_one, p_two):
    player_one_position = players_data[p_one].keys()
    player_two_position = players_data[p_two].keys()
    for post in player_one_position:
        if post in player_two_position:
            return True, post
    return False, ''


def players_battle(players_data, total_points, battle):
    player_one = battle[0]
    player_two = battle[1]
    if players_exist(players_data, player_one, player_two):
        start_battle, position = common_position(players_data, player_one, player_two)
        if start_battle:
            if total_points[player_one] > total_points[player_two]:
                del players_data[player_two]
                del total_points[player_two]

            elif total_points[player_one] < total_points[player_two]:
                del players_data[player_one]
                del total_points[player_one]


players_data = {}
players_total_points = {}

while True:
    line = input()
    if line == 'Season end':
        break
    elif ' -> ' in line:
        data = line.split(' -> ')
        init_player(players_data, data)
    elif ' vs ' in line:
        data = line.split(' vs ')
        players_battle(players_data, players_total_points, data)

for player, total_skills in sorted(players_total_points.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    print(f'{player}: {total_skills} skill')
    for position, skill in sorted(players_data[player].items(), key=lambda kvp: (-kvp[1], kvp[0])):
        print(f'- {position} <::> {skill}')
