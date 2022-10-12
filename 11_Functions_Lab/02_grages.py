def check_grade(grade_number):
    if 2 <= grade_number <= 2.99:
        return 'Fail'
    elif 3.00 <= grade_number <= 3.49:
        return 'Poor'
    elif 3.50 <= grade_number <= 4.49:
        return 'Good'
    elif 4.50 <= grade_number <= 5.49:
        return 'Very Good'
    elif 5.50 <= grade_number <= 6.00:
        return 'Excellent'


score = float(input())

print(check_grade(score))
