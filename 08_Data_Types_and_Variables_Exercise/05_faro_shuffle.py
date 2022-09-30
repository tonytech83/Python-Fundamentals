deck_of_cards = input().split()
number_of_shuffles = int(input())

for shuffle in range(number_of_shuffles):

    left_deck = deck_of_cards[:len(deck_of_cards) // 2]
    right_desk = deck_of_cards[len(deck_of_cards) // 2:]

    deck_after_shuffle = []

    for card in range(len(left_deck)):
        deck_after_shuffle.append(left_deck[card])
        deck_after_shuffle.append(right_desk[card])

    deck_of_cards = deck_after_shuffle

print(deck_after_shuffle)
