def is_palindrome(numbers):
    for number in numbers:
        print(number == number[::-1])


numbers = input().split(', ')

is_palindrome(numbers)
