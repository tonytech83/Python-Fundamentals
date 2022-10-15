def positive(received_numbers):
    return [number for number in received_numbers if int(number) >= 0]


def negative(received_numbers):
    return [number for number in received_numbers if int(number) < 0]


def even(received_numbers):
    return [number for number in received_numbers if int(number) % 2 == 0]


def odd(received_numbers):
    return [number for number in received_numbers if int(number) % 2 != 0]


def main():
    print(f"Positive: {', '.join(positive(numbers))}")
    print(f'Negative: {", ".join(negative(numbers))}')
    print(f'Even: {", ".join(even(numbers))}')
    print(f'Odd: {", ".join(odd(numbers))}')


numbers = [x for x in input().split(', ')]

main()
