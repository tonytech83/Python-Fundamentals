tasks = []

while True:
    task = input()

    if task == 'End':
        break

    new_task = task.split('-')

    priority = int(new_task[0])
    current_task = new_task[1]

    tasks.append((priority, current_task))

sorted_tasks = [task_data[1] for task_data in sorted(tasks)]

print(sorted_tasks)
