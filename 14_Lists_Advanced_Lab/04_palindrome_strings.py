def only_palindrome(word):
    if word == word[::-1]:
        return word


words = input().split()
searched_palindrome = input()

palindromes_list = [word for word in words if only_palindrome(word)]

print(palindromes_list)
print(f'Found palindrome {palindromes_list.count(searched_palindrome)} times')
