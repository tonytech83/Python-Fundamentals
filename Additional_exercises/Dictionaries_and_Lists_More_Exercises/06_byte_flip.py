# Python3 program to convert hexadecimal
# string to ASCII format string

def hex_to_ascii(string):
    """
    This function receives list of hex numbers in sting format.
    Iterates trough them one by one, converts sting into integer and converts integer into char form ASCII
    :param string: list
    :return:
    """
    # initialize the ASCII code string as empty.
    text = ''

    for digit in reversed(string):

        # change it into base 16 and
        # typecast as the character
        ch = chr(int(digit, 16))

        # add this char to final ASCII string
        text += ch

    return text


# collect ony elements with length equal 2 and reverse digits in every hexadecimal number
string_array = [x[::-1] for x in input().split() if len(x) == 2]

# print the ASCII string.
print(hex_to_ascii(string_array))
