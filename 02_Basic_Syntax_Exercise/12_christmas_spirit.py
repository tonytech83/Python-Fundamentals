decorations_count = int(input())
left_days = int(input())

christmas_spirit = 0
budget = 0

for day in range(1, left_days + 1):

    if day % 11 == 0:
        decorations_count += 2

    if day % 2 == 0:
        budget += decorations_count * 2
        christmas_spirit += 5

    if day % 3 == 0:
        budget += decorations_count * 8
        christmas_spirit += 13

    if day % 5 == 0:
        budget += decorations_count * 15
        christmas_spirit += 17
        if day % 3 == 0:
            christmas_spirit += 30

    if day % 10 == 0:
        christmas_spirit -= 20
        budget += 23

if left_days % 10 == 0:
    christmas_spirit -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {christmas_spirit}")
