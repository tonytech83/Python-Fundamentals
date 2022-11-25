import re


def license_plate_validation(current_plate):
    """
    This func checks if the license plate number meets the following conditions:
    - It is always exactly 8 characters long.
    - Its first 2 and last 2 characters are always uppercase Latin letters
    - The 4 characters in the middle are always digits
    :param current_plate: str
    :return: boolean
    """
    pattern = r'\b([A-Z]{2}\d{4}[A-Z]{2})'
    match = re.search(pattern, current_plate)
    if match:
        return True
    else:
        return False


def register(name, plate, license_plates):
    """
    This function register new name and plate and returns messages for any of conditions.
    :param name: str
    :param plate: str
    :param license_plates: dict
    :return: str
    """
    if name in license_plates:
        current_plate = license_plates[name]
        return f'ERROR: already registered with plate number {current_plate}'

    if not license_plate_validation(plate):
        return f'ERROR: invalid license plate {plate}'

    if plate in license_plates.values():
        return f'ERROR: license plate {plate} is busy'

    if name not in license_plates:
        license_plates[name] = plate
        return f'{name} registered {plate} successfully'


def unregister(name, license_plates):
    """
    This func unregistered received name if it is exists in license_plates dict.
    :param name: str
    :param license_plates: dict
    :return: str
    """
    if name in license_plates:
        del license_plates[name]
        return f'user {name} unregistered successfully'
    return f'ERROR: user {name} not found'


def output(license_plates):
    """
    This func prints all information from license_plates dict.
    :param license_plates: dict
    """
    result = ''
    for name, plate in license_plates.items():
        result += f'{name} => {plate}\n'
    return result


def execution(event_number):
    """
    Main function receives input from console, according split of input its colling register func or unregister func.
    :param event_number: int
    """
    license_plates = {}
    for _ in range(event_number):
        data = input().split()
        event = data[0]

        if event == 'register':
            name, license_plate = data[1], data[2]
            print(register(name, license_plate, license_plates))
        elif event == 'unregister':
            name = data[1]
            print(unregister(name, license_plates))

    print(output(license_plates))


number_of_commands = int(input())
execution(number_of_commands)
