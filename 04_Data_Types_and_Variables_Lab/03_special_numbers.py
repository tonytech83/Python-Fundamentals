number = int(input())

for num in range(1, number + 1):

    flag = False

    num = str(num).zfill(6)
    sum_of_digits = int(num[0]) + int(num[1]) + int(num[2]) + int(num[3]) + int(num[4]) + int(num[5])
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        flag = 'True'
        sum_of_digits = 0

    print(f'{int(num)} -> {flag}')
