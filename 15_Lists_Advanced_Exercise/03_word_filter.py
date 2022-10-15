words = [x for x in input().split()]

only_even_words = [word for word in words if len(word) % 2 == 0]

print(*only_even_words, sep='\n')
