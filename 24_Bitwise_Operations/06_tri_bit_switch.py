number = int(input())
position = int(input())

mask = 7 << position
result = number ^ mask

print(result)
