def loading_bar(number, bar):
    if number == 100:
        return bar
    else:
        for idx in range(0, 100 - number, 10):
            bar.remove("%")
            bar.append('.')
        return bar


bar = ['%'] * 10
percent_number = int(input())
loading_bar(percent_number, bar)

if percent_number == 100:
    print(f'{percent_number}% Complete!')
    print(f"[{''.join(bar)}]")
else:
    print(f"{percent_number}% [{''.join(bar)}]")
    print('Still loading...')
