first_int = int(input())
second_int = int(input())

print(f'Before:\na = {first_int}\nb = {second_int}')

first_int, second_int = second_int, first_int

print(f'After:\na = {first_int}\nb = {second_int}')
