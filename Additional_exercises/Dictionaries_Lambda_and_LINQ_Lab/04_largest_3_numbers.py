numbers = [int(x) for x in input().split()]

sorted_numbers = sorted(numbers, reverse=True)

for idx in range(len(sorted_numbers)):
    print(sorted_numbers[idx], end=' ')
    if idx == 2:
        break
