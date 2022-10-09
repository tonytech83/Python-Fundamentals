list_of_numbers = []

for _ in range(3):
    number = int(input())
    list_of_numbers.append(number)

if list(filter(lambda x: x == 0, list_of_numbers)):
    print('zero')
elif list(filter(lambda x: x < 0, list_of_numbers)):
    negative = list(filter(lambda x: x < 0, list_of_numbers))
    if len(negative) != 2:
        print('negative')
    else:
        print('positive')
elif list(filter(lambda x: x > 0, list_of_numbers)):
    print('positive')
