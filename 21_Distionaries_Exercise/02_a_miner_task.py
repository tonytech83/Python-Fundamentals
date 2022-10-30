miner_task = {}

while True:
    data = input()
    if data == 'stop':
        break
    value = int(input())
    if data not in miner_task:
        miner_task[data] = value
    else:
        miner_task[data] += value

for resource, quantity in miner_task.items():
    print(f'{resource} -> {quantity}')
