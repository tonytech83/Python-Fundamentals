number_of_chr = int(input())

sum_of_chars = 0

for char in range(number_of_chr):
    current_chr = input()
    sum_of_chars += ord(current_chr)

print(f'The sum equals: {sum_of_chars}')
