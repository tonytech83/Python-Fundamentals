from collections import deque

start_idx = int(input())
end_idx = int(input())

string = deque()

for char in range(start_idx, end_idx + 1):
    string.append(chr(char))

print(*string, sep=' ')
