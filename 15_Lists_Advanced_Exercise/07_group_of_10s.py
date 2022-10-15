def groups(sequence_of_numbers):
    current_group = 10
    while sequence_of_numbers:
        group = [num for num in sequence_of_numbers if num <= current_group]
        sequence_of_numbers = [x for x in sequence_of_numbers if x not in group]
        print(f"Group of {current_group}'s: {group}")
        current_group += 10


def main():
    sequence_of_numbers = [int(x) for x in input().split(', ')]
    groups(sequence_of_numbers)


main()
