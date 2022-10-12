def calculation(number_one, number_two, operator):
    if operator == 'multiply':
        return multiply(number_one, number_two)
    elif operator == 'divide':
        return divide(number_one, number_two)
    elif operator == 'add':
        return add(number_one, number_two)
    elif operator == 'subtract':
        return subtract(number_one, number_two)


def multiply(number_one, number_two):
    return number_one * number_two


def divide(number_one, number_two):
    return int(number_one / number_two)


def add(number_one, number_two):
    return number_one + number_two


def subtract(number_one, number_two):
    return number_one - number_two


user_operator = input()
num_one = int(input())
num_two = int(input())

print(calculation(num_one, num_two, user_operator))
