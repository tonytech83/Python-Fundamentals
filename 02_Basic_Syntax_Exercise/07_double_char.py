string = input()

while string != "End":

    if string == 'SoftUni':
        string = input()
        continue

    for letter in string:
        print(letter * 2, end='')

    print()

    string = input()
