string = input()

result = []

for idx, letter in enumerate(string):
    if 65 <= ord(letter) <= 90:
        result.append(idx)

print(result)
