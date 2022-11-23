numbers = [s for s in input().split()]

reversed_sum = 0

for number in numbers:
    reversed_sum += int(number[::-1])

print(reversed_sum)
