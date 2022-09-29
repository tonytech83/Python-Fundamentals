# global variables
EVEN = 'even'
ODD = 'odd'
NEGATIVE = 'negative'
POSITIVE = 'positive'

number_of_lines = int(input())

integers_list = []

for _ in range(number_of_lines):
    current_number = int(input())
    integers_list.append(current_number)

command = input()

filtered_numbers = []

for idx in range(len(integers_list)):
    if (command == EVEN and integers_list[idx] % 2 == 0 or
            command == ODD and integers_list[idx] % 2 != 0 or
            command == NEGATIVE and integers_list[idx] < 0 or
            command == POSITIVE and integers_list[idx] >= 0
    ):
        filtered_numbers.append(integers_list[idx])

print(filtered_numbers)
