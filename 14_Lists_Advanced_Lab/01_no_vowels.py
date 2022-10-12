text = input()
vowels = ['a', 'o', 'u', 'e', 'i']
result_text = [x for x in text if x.lower() not in vowels]

print(*result_text, sep='')
