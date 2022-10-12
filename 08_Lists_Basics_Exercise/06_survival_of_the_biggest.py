numbers = [int(x) for x in input().split()]
sorted_numbers = sorted(numbers)

count_to_remove = int(input())

removed_numbers = sorted_numbers[:count_to_remove]

for number in removed_numbers:
    if number in numbers:
        numbers.remove(number)

print(*numbers, sep=', ')
