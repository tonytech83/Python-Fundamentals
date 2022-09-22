year = int(input())

while True:
    year += 1
    year_to_set = set()

    for digit in str(year):
        year_to_set.add(int(digit))

    if len(str(year)) == len(year_to_set):
        print(year)
        break
