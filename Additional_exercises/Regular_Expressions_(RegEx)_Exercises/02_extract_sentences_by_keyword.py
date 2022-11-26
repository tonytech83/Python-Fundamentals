import re

word = input()
text = input()

# extract all sentences with word variable
sentence_pattern = rf'\b[^?.!]*\b{word}\b[^?.!]*'
matches = re.findall(sentence_pattern, text)

print('\n'.join(matches))

