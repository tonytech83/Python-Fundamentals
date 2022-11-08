text = input()

for char in range(len(text)):
    if text[char] == ':':
        print(f":{text[char + 1]}")
