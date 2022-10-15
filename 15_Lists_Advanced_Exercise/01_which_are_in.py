first_string = [x for x in input().split(', ')]
second_string = [x for x in input().split(', ')]

substrings = []

for first in first_string:
    for second in second_string:
        if first in second:
            substrings.append(first)
            break

print(substrings)
