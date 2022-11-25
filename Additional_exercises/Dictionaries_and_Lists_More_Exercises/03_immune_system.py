def fight(current_virus, immune_system):
    global initial_health
    global max_health

    if current_virus not in immune_system:
        immune_system[current_virus] = 1
    else:
        immune_system[current_virus] += 1

    virus_strength = sum([ord(x) for x in current_virus]) // 3
    if immune_system[current_virus] < 2:
        time_to_defeat = int(virus_strength * len(current_virus))
    elif immune_system[current_virus] == 2:
        time_to_defeat = int((virus_strength * len(current_virus)) // 3)
    else:
        time_to_defeat = immune_system[current_virus]

    print(f'Virus {current_virus}: {virus_strength} => {time_to_defeat} seconds')

    if time_to_defeat <= initial_health:
        initial_health -= time_to_defeat
        minutes = time_to_defeat // 60
        seconds = time_to_defeat % 60

        print(f'{current_virus} defeated in {minutes}m {seconds}s.')
        print(f'Remaining health: {int(initial_health)}')
        initial_health = int(initial_health * 1.2)
        if initial_health > max_health:
            initial_health = max_health
    else:
        initial_health -= time_to_defeat
        print('Immune System Defeated.')


initial_health = int(input())
max_health = initial_health
immune_system = {}

while True:
    if initial_health < 0:
        break

    virus = input()

    if virus == 'end':
        print(f'Final Health: {initial_health}')
        break
    else:
        fight(virus, immune_system)
