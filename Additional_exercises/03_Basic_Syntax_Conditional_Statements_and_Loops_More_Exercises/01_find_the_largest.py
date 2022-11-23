number = input()

number_to_array = []
new_number = []

for digit in number:
    number_to_array.append(int(digit))

for digit in range(len(number_to_array)):
    max_digit = max(number_to_array)
    new_number.append(max_digit)
    number_to_array.remove(max_digit)

print(*new_number, sep='')
