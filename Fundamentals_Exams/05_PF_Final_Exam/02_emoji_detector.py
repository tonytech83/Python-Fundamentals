import re

text = input()

# extract all digits from text string
digit_pattern = r'\d'
digits = re.findall(digit_pattern, text)

# multiply all digits to obtain cool_threshold
cool_threshold = 1
for digit in digits:
    cool_threshold = cool_threshold * int(digit)

# extract all hidden emojis form text string
emoji_pattern = r'(\:{2}|\*{2})([A-Z][a-z]{2,})\1'
matches = re.findall(emoji_pattern, text)

# create dictionary where to store all founded emojis
emojis = {}

# iterate through all founded emojis and calculates their coolness
for match in matches:
    emoji = match[0] + match[1] + match[0]
    emojis[emoji] = sum([ord(s) for s in match[1]])

print(f'Cool threshold: {cool_threshold}')
print(f'{len(emojis)} emojis found in the text. The cool ones are:')

for key, value in emojis.items():
    if value > cool_threshold:
        print(key)
