number = input()

number_to_array = []

for digit in number:
    number_to_array.append(digit)

for _ in range (len(number)):
    print(max(number_to_array), end='')
    number_to_array.remove(max(number_to_array))
