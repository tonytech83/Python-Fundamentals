text = input()

encrypted_text = ''

for char in text:
    encrypted_text += chr(ord(char) + 3)

print(encrypted_text)

# solution 1 with comprehension
# print(*[chr(ord(char) + 3) for char in text], sep='')
# solution 2 with comprehension
# print(''.join([chr(ord(char) + 3) for char in text]))
