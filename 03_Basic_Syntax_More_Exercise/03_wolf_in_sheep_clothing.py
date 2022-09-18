data = input().split(', ')

if data[- 1] == 'wolf':
    print('Please go away and stop eating my sheep')
else:
    for idx, animal in enumerate(reversed(data)):
        if animal == 'wolf':
            print(f'Oi! Sheep number {idx}! You are about to be eaten by a wolf!')
