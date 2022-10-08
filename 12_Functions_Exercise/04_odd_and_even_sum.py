def odd_even_sums(number):
    sum_of_odd_digits = []
    sum_of_even_digits = []

    for digit in number:
        if int(digit) % 2 == 0:
            sum_of_even_digits.append(int(digit))
        else:
            sum_of_odd_digits.append(int(digit))
    return sum(sum_of_even_digits), sum(sum_of_odd_digits)


numbers = input()

sum_of_even, sum_of_odd = odd_even_sums(numbers)
print(f'Odd sum = {sum_of_odd}, Even sum = {sum_of_even}')
