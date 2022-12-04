def check_unique(current_elements):
    if len(current_elements) == len(set(current_elements)):
        return True
    return False


def increase_even(current_elements):
    for idx, digit in enumerate(current_elements):
        if digit % 2 == 0:
            current_elements[idx] += 2
    return current_elements


def increase_odd(current_elements):
    for idx, digit in enumerate(current_elements):
        if digit % 2 != 0:
            current_elements[idx] += 3
    return current_elements


while True:
    line = input()
    if line == 'stop playing':
        break

    elements = [int(x) for x in line.split()]

    if check_unique(elements):
        the_elements = increase_even(elements)
        print(f'Unique list: ', end='')
        print(*sorted(the_elements), sep=',')
        print(f'Output: {sum(the_elements) / len(the_elements):.2f}')
    else:
        the_elements = increase_odd(elements)
        print(f'Non-unique list: ', end='')
        print(*sorted(the_elements), sep=':')
        print(f'Output: {sum(the_elements) / len(the_elements):.2f}')
