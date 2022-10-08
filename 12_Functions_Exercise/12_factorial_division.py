def recur_factorial(number):
    if number == 1:
        return number
    else:
        return number * recur_factorial(number - 1)


number_one = int(input())
number_two = int(input())

factorial_one = recur_factorial(number_one)
factorial_two = recur_factorial(number_two)

result = factorial_one // factorial_two

print(f'{result:.2f}')
