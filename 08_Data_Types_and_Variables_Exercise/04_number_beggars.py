money = []

for number in input().split(', '):
    money.append(int(number))

beggars_count = int(input())

sums_for_beggars = [0] * beggars_count

while len(money) != 0:
    for beggar in range(beggars_count):
        sums_for_beggars[beggar] += money[0]
        money.pop(0)

        if len(money) == 0:
            break

print(sums_for_beggars)
