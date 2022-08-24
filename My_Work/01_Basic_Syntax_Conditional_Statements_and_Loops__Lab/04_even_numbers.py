n = int(input())

all_even = True

for num in range(n):
    number = int(input())
    if number % 2 == 0:
        pass
    else:
        all_even = False
        print(f'{number} is odd!')
        break

if all_even:
    print('All numbers are even.')
