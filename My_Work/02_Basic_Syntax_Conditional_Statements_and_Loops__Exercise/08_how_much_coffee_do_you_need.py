event = input()

coffee_counter = 0

need_extra_sleep = False

while event != 'END':

    if ord(event[0]) in range(65, 91):
        coffee = 2
    else:
        coffee = 1

    if coffee_counter >= 5:
        need_extra_sleep = True
        break

    event = event.lower()

    if event == 'dog':
        coffee_counter += coffee
    elif event == 'coding':
        coffee_counter += coffee
    elif event == 'cat':
        coffee_counter += coffee
    elif event == 'movie':
        coffee_counter += coffee

    event = input()

if need_extra_sleep:
    print(f'You need extra sleep')
else:
    print(coffee_counter)
