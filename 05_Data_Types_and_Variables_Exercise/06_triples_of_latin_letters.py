letters_number = int(input())

start_letter = 97
end_letter = 97 + letters_number

for first in range(start_letter, end_letter):
    for second in range(start_letter, end_letter):
        for third in range(start_letter, end_letter):
            print(chr(first), chr(second), chr(third), sep='')
