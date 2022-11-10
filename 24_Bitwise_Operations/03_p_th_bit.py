number = int(input())
idx = int(input())
number_to_binary = bin(number)[2:]

reversed_bin_numer = number_to_binary[::-1]

try:
    print(reversed_bin_numer[idx])
except IndexError:
    print('0')
