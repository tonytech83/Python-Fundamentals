n = int(input())

numbers = []

for _ in range(n):
    num = int(input())
    numbers.append(num)

print(f'Sum = {sum(numbers)}')
print(f'Min = {min(numbers)}')
print(f'Max = {max(numbers)}')
print(f'Average = {(sum(numbers) / len(numbers))}')
