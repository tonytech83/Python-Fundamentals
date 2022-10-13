numbers = list(map(int, input().split(', ')))

list_of_idx = [num for num in range(len(numbers)) if numbers[num] % 2 == 0]

print(list_of_idx)
