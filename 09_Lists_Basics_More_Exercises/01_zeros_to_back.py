numbers = [int(x) for x in input().split(', ')]

for digit in range(numbers.count(0)):
    numbers.remove(0)
    numbers.append(0)

print(numbers)
