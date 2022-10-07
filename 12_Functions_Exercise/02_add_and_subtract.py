def sum_numbers(first_number, second_number):
    return first_number + second_number


def subtract(sum_of_first_two, third_number):
    return sum_of_first_two - third_number


def add_and_subtract(first_number, second_number, third_number):
    sum_of_first_two = sum_numbers(first_number, second_number)
    result = subtract(sum_of_first_two, third_number)
    return result


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

print(add_and_subtract(number_1, number_2, number_3))
