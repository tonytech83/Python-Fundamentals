circle_of_people = [x for x in input().split()]
execute_person = int(input())

order_of_executions = []
counter = 0
index = 0

while len(circle_of_people) > 0:
    counter += 1

    if counter % execute_person == 0:
        order_of_executions.append(circle_of_people.pop(index))
    else:
        index += 1

    if index >= len(circle_of_people):
        index = 0

print(str(order_of_executions).replace(' ', '').replace('\'', ''))
