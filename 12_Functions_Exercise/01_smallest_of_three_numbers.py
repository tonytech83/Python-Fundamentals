def find_smallest_number(all_numbers):
    return min(all_numbers)


all_numbers = []

for _ in range(3):
    number = int(input())
    all_numbers.append(number)

print(find_smallest_number(all_numbers))
