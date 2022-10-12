events_per_day = [x for x in input().split('|')]

energy = 100
coins = 100
should_close = False

for event in events_per_day:

    event_type, event_value = event.split('-')

    if event_type == 'rest':
        current_energy = energy
        energy += int(event_value)
        if energy > 100:
            energy = 100
        gained_energy = energy - current_energy
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {energy}.')

    elif event_type == 'order':

        earned_coins = int(event_value)

        if energy >= 30:
            coins += earned_coins
            energy -= 30
            print(f'You earned {earned_coins} coins.')
        else:
            energy += 50
            print('You had to rest!')

    else:

        spent_coins = int(event_value)

        if coins >= spent_coins:
            coins -= spent_coins
            print(f'You bought {event_type}.')
        else:
            should_close = True
            print(f'Closed! Cannot afford {event_type}.')
            break

if not should_close:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')
