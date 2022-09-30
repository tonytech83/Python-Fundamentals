factor = int(input())
count = int(input())

list_of_numbers = []

for num in range(1, count + 1):
    list_of_numbers.append(num * factor)

print(list_of_numbers)
