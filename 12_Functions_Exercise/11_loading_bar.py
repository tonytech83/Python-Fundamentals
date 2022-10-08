def loading_bar(number, bar):
    for _ in range(0, 100 - number, 10):
        bar.remove("%")
        bar.append('.')
    return bar


percent_number = int(input())

if percent_number == 100:
    print(f'{percent_number}% Complete!\n[%%%%%%%%%%]')
else:
    bar = ['%'] * 10
    loading_bar(percent_number, bar)
    print(f"{percent_number}% [{''.join(bar)}]\nStill loading...")
