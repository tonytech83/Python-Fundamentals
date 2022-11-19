def car_drive(current_command):
    """
    This function manipulates mileages and fuel of current car.
    :param current_command: str
    :return: str
    """
    global cars
    current_car = current_command[1]
    distance = int(current_command[2])
    spent_fuel = int(current_command[3])

    if current_car in cars:
        if cars[current_car][1] < spent_fuel:
            return 'Not enough fuel to make that ride'
        else:
            cars[current_car][0] += distance
            cars[current_car][1] -= spent_fuel
            return f'{current_car} driven for {distance} kilometers. {spent_fuel} liters of fuel consumed.'


def car_refuel(current_command):
    """
    This function received amount of fuel for refill and manipulates fuel for current car.
    :param current_command: str
    :return: str
    """
    global cars
    current_car = current_command[1]
    fuel_to_refill = int(current_command[2])
    current_fuel = cars[current_car][1]
    diff = 75 - current_fuel
    if diff < fuel_to_refill:
        cars[current_car][1] += diff
        return f'{current_car} refueled with {diff} liters'
    else:
        cars[current_car][1] += fuel_to_refill
        return f'{current_car} refueled with {fuel_to_refill} liters'


def car_revert(current_command):
    """
    This function decrease the mileage of the given car with the given kilometer.
    If the mileage becomes less than 10 000km after it is decreased, just set it to 10 000km.
    :param current_command: str
    :return: str
    """
    global cars
    current_car = current_command[1]
    kilometers = int(current_command[2])
    cars[current_car][0] -= kilometers
    if cars[current_car][0] < 10000:
        cars[current_car][0] = 10000
    else:
        new_mileage(current_car, kilometers)


def new_mileage(renewed_car, reverted_kilometers):
    """
    This function only prints if its calling function has unfulfilled condition
    :param renewed_car: str
    :param reverted_kilometers: int
    """
    print(f'{renewed_car} mileage decreased by {reverted_kilometers} kilometers')


def car_for_sell():
    """
    This function check is mileage of any car is more than 100000 and deletes it
    :return: str
    """
    global cars
    for key, value in cars.items():
        if value[0] >= 100000:
            del cars[key]
            return key


number_of_cars = int(input())

cars = {}

for _ in range(number_of_cars):
    car, mileage, fuel = input().split('|')
    cars[car] = []
    cars[car].extend([int(mileage), int(fuel)])

while True:
    command = input().split(' : ')
    action = command[0]
    if action == 'Stop':
        break
    elif action == 'Drive':
        print(car_drive(command))
        car_to_sell = car_for_sell()
        if car_to_sell:
            print(f'Time to sell the {car_to_sell}!')
    elif action == 'Refuel':
        print(car_refuel(command))
    elif action == 'Revert':
        car_revert(command)

for car, info in cars.items():
    print(f'{car} -> Mileage: {info[0]} kms, Fuel in the tank: {info[1]} lt.')
