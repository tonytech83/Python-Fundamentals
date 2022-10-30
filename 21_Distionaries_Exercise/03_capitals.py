countries = input().split(', ')
capitals = input().split(', ')

my_dict = dict(zip(countries, capitals))

for key, value in my_dict.items():
    print(f'{key} -> {value}')
