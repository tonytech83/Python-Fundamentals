number_of_lines = int(input())
searched_word = input()

strings_list = []
strings_containing_word = []

for _ in range(number_of_lines):
    current_string = input()
    strings_list.append(current_string)

for string in strings_list:
    if searched_word in string:
        strings_containing_word.append(string)

print(strings_list)
print(strings_containing_word)
