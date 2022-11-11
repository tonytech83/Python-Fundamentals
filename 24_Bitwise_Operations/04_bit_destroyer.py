n = int(input())
position = int(input())

mask = ~(1 << position)

new_number = n & mask

print(new_number)
