# https://www.youtube.com/watch?v=N-AlTemCnMc&t=1495s

numbers = [int(x) for x in input().split()]

max_len = 0
last_idx = -1
length = [0] * len(numbers)
prev = [0] * len(numbers)

for num in range(len(numbers)):
    length[num] = 1
    prev[num] = -1
    for idx in range(num):
        if numbers[idx] < numbers[num] and length[idx] + 1 > length[num]:
            length[num] = 1 + length[idx]
            prev[num] = idx
    if length[num] > max_len:
        max_len = length[num]
        last_idx = num

longest_seq = []
while last_idx != -1:
    longest_seq.append(numbers[last_idx])
    last_idx = prev[last_idx]

print(*longest_seq[::-1])
