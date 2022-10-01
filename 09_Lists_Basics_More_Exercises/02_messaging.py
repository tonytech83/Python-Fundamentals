sequence_of_numbers = [x for x in input().split()]

received_string = [x for x in input()]

words_to_letters = []
for word in received_string:
    for letter in word:
        words_to_letters.append(letter)

message = []

for number in sequence_of_numbers:

    current_idx = 0

    for digit in number:
        current_idx += int(digit)

    if current_idx >= len(words_to_letters):
        current_idx -= len(words_to_letters)

    message.append(words_to_letters[current_idx])
    words_to_letters.pop(current_idx)

print(*message, sep='')
