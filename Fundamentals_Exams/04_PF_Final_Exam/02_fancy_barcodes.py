import re

barcodes_count = int(input())

# RegEx barcode validation:
# It is surrounded by a "@" followed by one or more "#".
# It is at least 6 characters long (without the surrounding "@" or "#").
# It starts with a capital letter.
# It contains only letters (lower and upper case) and digits.
# It ends with a capital letter.
barcode_pattern = r'(@#+)([A-Z][A-Za-z0-9]{4,}[A-Z])'

for _ in range(barcodes_count):
    sequence = input()
    match = re.search(barcode_pattern, sequence)

    if match:
        barcode = match.group(2)
        # RegEx for product group extraction
        # The product group is obtained by concatenating all the digits found in the barcode.
        # If there are no digits present in the barcode, the default product group is "00".
        extract_digits = r'(\d+)'
        product_group_match = re.findall(extract_digits, barcode)

        if product_group_match:
            product_group = ''
            for digit_match in product_group_match:
                product_group += digit_match
            print(f'Product group: {product_group}')
        else:
            print('Product group: 00')

    else:
        print('Invalid barcode')
