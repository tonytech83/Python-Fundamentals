first_character = ord(input())
second_character = ord(input())
random_string = input()

result = 0

for char in random_string:
    if ord(char) in range(first_character + 1, second_character):
        result += ord(char)

print(result)
