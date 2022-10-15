secret_message = input().split()

for word in secret_message:
    decoded_word = []

    # only take numbers
    number = [int(x) for x in word if x.isdigit()]
    string = [str(integer) for integer in number]
    a_string = "".join(string)
    char = chr(int(a_string))

    decoded_word.append(char)

    # only take letters
    characters = [x for x in word if x.isalpha()]
    characters[0], characters[-1] = characters[-1], characters[0]
    decoded_word += characters
    print(*decoded_word, sep='', end=' ')
