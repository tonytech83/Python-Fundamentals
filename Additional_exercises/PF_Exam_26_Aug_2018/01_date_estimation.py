from datetime import datetime

date_str = '2018-08-26'
today = datetime.strptime(date_str, '%Y-%m-%d')

single_date = input()
the_date = datetime.strptime(single_date, '%Y-%m-%d')

delta = today - the_date

if delta.days > 0:
    print('Passed')
elif delta.days == 0:
    print(f'Today date')
else:
    print(f'{abs(delta.days) + 1} days left')