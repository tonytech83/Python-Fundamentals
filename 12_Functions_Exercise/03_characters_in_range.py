def characters_between(first, second):
    characters = []

    for char in range(ord(first) + 1, ord(second)):
        characters.append(chr(char))

    return characters


first_chr = input()
second_chr = input()

print(*(characters_between(first_chr, second_chr)), sep=' ')
