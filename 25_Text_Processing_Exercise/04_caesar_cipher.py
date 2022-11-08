text = input()

encrypted_text = ''

for char in text:
    encrypted_text += chr(ord(char) + 3)

print(encrypted_text)
