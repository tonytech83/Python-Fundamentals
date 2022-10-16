def increase_decrease(removed_value):
    global distances
    distances = [value + removed_value if value <= removed_value else value - removed_value for value in distances]
    removed_pokemons.append(removed_value)


distances = [int(x) for x in input().split()]
removed_pokemons = []

while distances:
    idx = int(input())
    if idx < 0:
        removed_value = distances.pop(0)
        last_value = distances[-1]
        distances.insert(0, last_value)
        increase_decrease(removed_value)
    elif idx > len(distances) - 1:
        removed_value = distances.pop(-1)
        first_value = distances[0]
        distances.append(first_value)
        increase_decrease(removed_value)
    else:
        removed_value = distances.pop(idx)
        increase_decrease(removed_value)

print(sum(removed_pokemons))
