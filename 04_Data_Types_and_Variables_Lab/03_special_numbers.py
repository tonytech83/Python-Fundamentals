number = int(input())
len_of_number = len(str(number))

for num in range(1, number + 1):

    sum_of_digits = 0
    flag = False

    num = str(num)

    for digit in num:
        sum_of_digits += int(digit)

    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        flag = True
        sum_of_digits = 0

    print(f'{int(num)} -> {flag}')
