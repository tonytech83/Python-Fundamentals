company_users = {}

while True:
    line = input()
    if line == 'End':
        break

    company_name, employee_id = line.split(' -> ')
    if company_name not in company_users:
        company_users[company_name] = []

    if employee_id not in company_users[company_name]:
        company_users[company_name].append(employee_id)

for name, employees in company_users.items():
    print(name)
    for user in employees:
        print(f'-- {user}')
