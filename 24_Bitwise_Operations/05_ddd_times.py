array_of_integers = [int(x) for x in input().split()]
result = 0

for digit in array_of_integers:
    result = result ^ digit

print(result)
