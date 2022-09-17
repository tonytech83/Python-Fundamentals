person_age = int(input())

drink = ''

if person_age <= 14:
    drink = 'toddy'
elif person_age <= 18:
    drink = 'coke'
elif person_age <= 21:
    drink = 'beer'
else:
    drink = 'whisky'

print(f'drink {drink}')
