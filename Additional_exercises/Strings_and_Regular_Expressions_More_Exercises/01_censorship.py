import re

word = input()
sentence = input()

sentence = re.sub(rf'{word}', f'*' * len(word), sentence)

print(sentence)
