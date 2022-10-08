def recur_factorial(number_1):
    if number_1 == 1:
        return number_1
    else:
        return number_1 * recur_factorial(number_1 - 1)


number_one = int(input())
number_two = int(input())

factorial_one = recur_factorial(number_one)
factorial_two = recur_factorial(number_two)

result = factorial_one // factorial_two

print(f'{result:.2f}')
