import re

text = input()

# prepared pattern finding hidden word pairs
pattern = r'([@#])([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1'
matches = re.findall(pattern, text)

# check if found matches and print the proper message
if matches:
    print(f"{len(matches)} word pairs found!")
else:
    print('No word pairs found!')

# created new list which should store the pair of words if second one spelled backward,
# is the same as the first word and vice versa (casing matters!)
mirror_words = []
for match in matches:
    if match[1] == match[2][::-1]:
        mirror_words.append(f'{match[1]} <=> {match[2]}')

# if found any mirror words, print them separated by ', '
if mirror_words:
    print('The mirror words are:')
    print(', '.join(mirror_words))
else:
    print('No mirror words!')
