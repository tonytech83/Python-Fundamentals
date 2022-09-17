event = input()

events = ['coding', 'dog', 'cat', 'movie']
coffees = 0

while event != "END":

    if event.lower() in events:
        if 65 <= ord(event[0]) <= 90:
            coffee = 2
        else:
            coffee = 1

        coffees += coffee

    event = input()

if coffees <= 5:
    print(coffees)
else:
    print('You need extra sleep')
