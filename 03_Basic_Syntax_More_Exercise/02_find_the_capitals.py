string = input()

capital_letters_list = []

for idx, letter in enumerate(string):
    if 65 <= ord(letter) <= 90:
        capital_letters_list.append(idx)

print(capital_letters_list)
