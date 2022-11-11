def uninterrupted_match_length(left, right, symbol):
    """
    This function takes only valid ticket and
    finds the uninterrupted match length of winning symbol in both halves of the ticket.
    The uninterrupted match length of symbol is less than 10
    :param right: str
    :param left: str
    :param symbol: str
    :return: Message with ticket and the uninterrupted match length of symbol / Message whit ticket
    """
    left_max_count = 0
    right_max_count = 0

    left_count = 0
    for char in left:
        if char == symbol:
            left_count += 1
            if left_count > left_max_count:
                left_max_count = left_count
        else:
            left_count = 0

    right_count = 0
    for char in right:
        if char == symbol:
            right_count += 1
            if right_count > right_max_count:
                right_max_count = right_count
        else:
            right_count = 0
    if left_max_count >= 6 and right_max_count >= 6:
        match_length = min(left_max_count, right_max_count)
        return f'ticket "{ticket}" - {match_length}{symbol}'
    else:
        return f'ticket "{ticket}" - no match'


def winning_ticket(current_ticket):
    """
    This function check if the current ticket contains winning symbol at least 6 times in both halves of the ticket.
    :param current_ticket: srt
    :return: Print the winning ticket or print message if symbol is not repeated at least 6 times
    """
    global winning_symbols
    searched_symbols = [symbol for symbol in winning_symbols if symbol in current_ticket]
    symbols_dict = {}
    if searched_symbols:
        for symbol in searched_symbols:
            symbols_dict[symbol] = current_ticket.count(symbol)

        symbols_dict = sorted(symbols_dict.items(), key=lambda x: -x[1])
        match_symbol = symbols_dict[0][0]
        left_side = current_ticket[:10].count(match_symbol)
        right_side = current_ticket[10:].count(match_symbol)
        if left_side < 6 or right_side < 6:
            print(f'ticket "{current_ticket}" - no match')

        elif left_side > 9 and right_side > 9:
            print(f'ticket "{current_ticket}" - 10{match_symbol} Jackpot!')

        elif left_side >= 6 and right_side >= 6:
            print(uninterrupted_match_length(current_ticket[:10], current_ticket[10:], match_symbol))

    else:
        print(f'ticket "{current_ticket}" - no match')


# collection of tickets separated by commas and spaces (one or many)
tickets = [t.strip() for t in input().split(', ')]

winning_symbols = ['@', '#', '$', '^']

for ticket in tickets:
    if len(ticket) != 20:
        print('invalid ticket')
    else:
        winning_ticket(ticket.strip())
