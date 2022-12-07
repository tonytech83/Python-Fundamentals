import re


def valid_price(number):
    """
    This function checks the price is valid float or int
    :param number: float
    :return: boolean
    """
    pattern = r'^(([1-9][0-9]*)\.?(\d{2})?)$'
    match = re.search(pattern, number)

    if match:
        return True
    return False


def store_book(data):
    """
    This func validates book info is OK and add it to bookstore dict
    :param data: str
    """
    global bookstore

    info, chapters = data.split(' -> ')
    info = info.split()

    if len(info) == 3 and valid_price(info[2]):
        title, author, price = info[0], info[1], info[2]
        chapters = [x for x in chapters.split(', ')]

        if title not in bookstore:
            bookstore[title] = [author, float(price), chapters]


def sold_book(book):
    """
    This function check if book is in bookstore and if yes add it to sold_book list, if no print message
    :param book: str
    """
    global total_money
    global sold_books

    book_request = book

    if book_request in bookstore:
        total_money += bookstore[book_request][1]
        chapters_count = len(bookstore[book_request][2])
        current_author = bookstore[book_request][0]
        sold_books.append(f'SOLD: {book_request} with author {current_author}. Chapters in the book {chapters_count}')
    else:
        print('No such book here')


def output():
    """
    This function prints every sold book and at the end prints sum of all sold books.
    """
    global total_money
    global sold_books

    if sold_books:
        for sale in sold_books:
            print(sale)
        print(f'Money: {total_money:.2f}')
    else:
        print('Bad day :(')


# store books
bookstore = {}
# sum of all sold books prices
total_money = 0
# store every sold book
sold_books = []


def main():
    # read lines from console till command 'on work'
    while True:
        book_info = input()
        if book_info == 'on work':
            break
        store_book(book_info)

    # read lines from console till command 'end work' and before brake calls output function
    while True:
        book_to_sold = input()
        if book_to_sold == 'end work':
            output()
            break
        sold_book(book_to_sold)


main()
