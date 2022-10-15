def fill_the_shells(number_of_electrons):
    shells = []
    idx = 1
    while True:
        added_electrons = 2 * idx ** 2
        shells.append(added_electrons)
        idx += 1
        number_of_electrons -= added_electrons
        if number_of_electrons < 2 * idx ** 2:
            if number_of_electrons == 0:
                break
            else:
                shells.append(number_of_electrons)
                break
    return shells


def main():
    number_of_electrons = int(input())
    print(fill_the_shells(number_of_electrons))


main()
