number_for_check = int(input())

is_prime = True

for divisor in range(2, number_for_check):
    if number_for_check % divisor == 0:
        is_prime = False

print(is_prime)
