population = [int(x) for x in input().split(', ')]
minimum_wealth = int(input())

if sum(population) // len(population) < minimum_wealth:
    print(f'No equal distribution possible')
else:
    for group in population:
        idx = population.index(group)
        if group < minimum_wealth:
            wealthiest_group = max(population)
            idx_wealthiest = population.index(max(population))
            population[idx] += minimum_wealth - group
            population[idx_wealthiest] -= minimum_wealth - group

    print(population)
