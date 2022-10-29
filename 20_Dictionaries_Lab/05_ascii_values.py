lst_of_chr = [x for x in input().split(', ')]
lst_of_ascii = [ord(x) for x in lst_of_chr]

print(dict(zip(lst_of_chr, lst_of_ascii)))
