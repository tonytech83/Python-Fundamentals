sequence_of_numbers = [int(x) for x in input().split()]

special_num, power = input().split()

while int(special_num) in sequence_of_numbers:

    idx = sequence_of_numbers.index(int(special_num))
    left = sequence_of_numbers[:(idx - int(power))]
    right = sequence_of_numbers[(idx + int(power) + 1):]

    if idx == 0:
        sequence_of_numbers = right
    elif len(sequence_of_numbers) <= int(power):
        sequence_of_numbers = []
    else:
        sequence_of_numbers = left + right

print(sum(sequence_of_numbers))
