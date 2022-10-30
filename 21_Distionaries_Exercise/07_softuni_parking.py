def registration(parking_lot, command):
    username = command[1]
    license_number = command[2]
    if username not in parking_lot:
        parking_lot[username] = license_number
        print(f'{username} registered {license_number} successfully')
    else:
        print(f'ERROR: already registered with plate number {license_number}')


def unregistration(parking_lot, command):
    username = command[1]
    if username not in parking_lot:
        print(f'ERROR: user {username} not found')
    else:
        parking_lot.pop(username)
        print(f'{username} unregistered successfully')


number_of_commands = int(input())

parking = {}

for _ in range(number_of_commands):
    command = input().split()
    event = command[0]

    if event == 'register':
        registration(parking, command)
    elif event == 'unregister':
        unregistration(parking, command)

for key, value in parking.items():
    print(f'{key} => {value}')
