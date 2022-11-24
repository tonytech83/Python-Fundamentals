numbers = [int(x) for x in input().split()]

# remove all odd numbers
numbers = [x for x in numbers if x % 2 == 0]

# average of numbers list
average = sum(numbers) / len(numbers)

for idx, num in enumerate(numbers):
    if num > average:
        numbers[idx] += 1
    else:
        numbers[idx] -= 1

print(*numbers, sep=' ')
