employees_happiness = list(map(int, input().split(' ')))
happiness_improvement_factor = int(input())

happiness_after_multiply = [factor * happiness_improvement_factor for factor in employees_happiness]

average_happiness = sum(happiness_after_multiply) / len(employees_happiness)

list_of_happy_employees = list(filter(lambda happiness: happiness > average_happiness, happiness_after_multiply))

if len(list_of_happy_employees) >= len(employees_happiness) / 2:
    print(f'Score: {len(list_of_happy_employees)}/{len(employees_happiness)}. Employees are happy!')
else:
    print(f'Score: {len(list_of_happy_employees)}/{len(employees_happiness)}. Employees are not happy!')
