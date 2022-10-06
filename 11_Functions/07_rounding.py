def round_numbers(lst_of_numbers):
    rounded_numbers = []
    for number in lst_of_numbers:
        rounded_numbers.append(round(number))
    return rounded_numbers


lst_of_numbers = [float(x) for x in input().split()]

print(round_numbers(lst_of_numbers))
