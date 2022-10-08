sequence_of_numbers = [int(x) for x in input().split()]

only_even_numbers = filter(lambda x: x % 2 == 0, sequence_of_numbers)

print(list(only_even_numbers))
