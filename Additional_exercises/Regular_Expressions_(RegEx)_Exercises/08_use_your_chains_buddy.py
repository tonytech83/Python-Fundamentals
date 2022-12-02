import re

html = input()

# get the text from all between <p> and </p>
pattern = r'<p>(.*?)</p>'
matches = re.findall(pattern, html)

message = ''

for match in matches:
    # replace all characters which are not small letters and numbers with a whitespace
    match = re.sub('[^a-z0-9]', ' ', match)

    # replace all multiple whitespaces with single one
    match = re.sub('\s+', ' ', match)

    word = ''

    for char in match:
        # whitespace remains whitespace
        if char == ' ':
            word += char
            continue

        # digits remains digits
        if 48 <= ord(char) <= 57:
            word += char
            continue

        # all letters from a to m are converted to letters from n to z (a  n; b  o; … m  z)
        # the letters from n to z are converted to letters from a to m (n  a; o  b; … z  m)
        if ord(char) > 109:
            word += chr(ord(char) - 13)
        else:
            word += chr(ord(char) + 13)

    message += word

print(message)
