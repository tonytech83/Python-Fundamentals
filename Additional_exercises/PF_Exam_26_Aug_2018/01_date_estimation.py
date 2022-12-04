from datetime import datetime

date_str = '2018-08-26'
# convert string to date object
today = datetime.strptime(date_str, '%Y-%m-%d')

single_date = input()
# convert string to date object
the_date = datetime.strptime(single_date, '%Y-%m-%d')

# difference between dates in timedelta
delta = today - the_date

if delta.days > 0:
    print('Passed')
elif delta.days == 0:
    print(f'Today date')
else:
    print(f'{abs(delta.days) + 1} days left')