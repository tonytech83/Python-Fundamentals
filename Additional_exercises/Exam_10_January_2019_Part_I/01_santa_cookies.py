# can't check the exam in judge because there isn't python test
# both examples from the condition are OK

amount_of_batches = int(input())

SINGLE_COOKIE_IN_GRAMS = 25
CUP = 140
SMALL_SPOON = 10
BIG_SPOON = 20
COOKIES_PER_BOX = 5

total_boxes = 0

for batch in range(amount_of_batches):
    flour = int(input())
    sugar = int(input())
    cocoa = int(input())

    flour_cups = flour // CUP
    sugar_spoons = sugar // BIG_SPOON
    cocoa_spoons = cocoa // SMALL_SPOON

    if flour_cups <= 0 or sugar_spoons <= 0 or cocoa_spoons <= 0:
        print('Ingredients are not enough for a box of cookies.')
        continue

    cookies = ((CUP + BIG_SPOON + SMALL_SPOON) * min(flour_cups, sugar_spoons, cocoa_spoons)) // SINGLE_COOKIE_IN_GRAMS
    cookies_per_box = cookies // COOKIES_PER_BOX
    print(f'Boxes of cookies: {cookies_per_box}')
    total_boxes += cookies_per_box

print(f'Total boxes: {total_boxes}')
