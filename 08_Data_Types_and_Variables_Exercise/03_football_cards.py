team_a = list('A-' + str(x) for x in range(1, 12))
team_b = list('B-' + str(x) for x in range(1, 12))

game_terminated = False

cards = input().split()

for card in cards:
    if card in team_a:
        team_a.remove(card)
    elif card in team_b:
        team_b.remove(card)

    if len(team_a) < 7 or len(team_b) < 7:
        game_terminated = True
        break

print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')

if game_terminated:
    print('Game was terminated')
