lst = input().split(', ')

sheep_in_danger = False
next_animal = len(lst)

for animal in lst:
    next_animal -= 1
    if animal == 'wolf':
        if next_animal > 0:
            sheep_in_danger = True
            break

if sheep_in_danger:
    print(f'Oi! Sheep number {next_animal}! You are about to be eaten by a wolf!')
else:
    print(f'Please go away and stop eating my sheep')
