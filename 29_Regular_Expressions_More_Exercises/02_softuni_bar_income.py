import re


def extract_name(data):
    """
    This function extract valid name from data string.
    Valid name should be surrounded by '%' and must start with a capital letter, followed by lower-case letters.
    :param data: str
    :return: str
    """
    pattern = r'(^|(?<=%))(?P<name>[A-Z][a-z]+)(?=%)'
    current_name = re.search(pattern, data)
    if current_name is not None:
        return current_name.group('name')


def extract_item(data):
    """
    This function extract valid item from data string.
    Valid product contains any word character (not only letters) and must be surrounded by '<' and '>'.
    :param data: str
    :return: str
    """
    pattern = r'(?<=<)(?P<item>[A-Za-z0-9\-\_\.]+)(?=>)'
    current_item = re.search(pattern, data)
    if current_item is not None:
        return current_item.group('item')


def extract_count(data):
    """
    This function extract valid count of items from data string.
    Valid count is an integer, surrounded by '|'.
    :param data: str
    :return: float
    """
    pattern = r'(?<=\|)(?P<count>\d+)(?=\|)'
    current_count = re.search(pattern, data)
    if current_count is not None:
        return float(current_count.group('count'))


def extract_price(data):
    """
    This function extract valid price of items from data string.
    Valid price is any real number followed by '$'.
    :param data: str
    :return: float
    """
    pattern = r'(?P<price>(\d+)\.?\d+)(?=\$)'
    current_price = re.search(pattern, data)
    if current_price is not None:
        return float(current_price.group('price'))


total_income = 0
while True:
    line = input()
    if line == 'end of shift':
        break

    name = extract_name(line)
    item = extract_item(line)
    count = extract_count(line)
    price = extract_price(line)
    if name and item and count and price:
        total_price = count * price
        total_income += total_price
        print(f'{name}: {item} - {total_price:.2f}')

print(f'Total income: {total_income:.2f}')
