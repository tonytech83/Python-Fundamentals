version = [int(x) for x in input().split('.')]

version[-1] += 1

for idx in range(len(version) - 1, -1, -1):
    if version[idx] > 9:
        version[idx] = 0
        version[idx - 1] += 1

print(*version, sep='.')
