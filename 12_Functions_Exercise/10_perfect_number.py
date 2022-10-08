def is_perfect_number(current_number):
    divisors = []
    for divisor in range(1, current_number):
        if current_number % divisor == 0:
            divisors.append(divisor)

    if sum(divisors) == current_number:
        return True
    return False


number = int(input())

if is_perfect_number(number):
    print('We have a perfect number!')
else:
    print("It's not so perfect.")
