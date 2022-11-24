numbers = [int(x) for x in input().split()]

left_fold = (numbers[:(len(numbers) // 4)])[::-1]
right_fold = (numbers[(len(numbers) - (len(numbers) // 4)):])[::-1]

numbers_lst = numbers[(len(numbers) // 4):(len(numbers) - (len(numbers) // 4))]
sub_list = left_fold + right_fold

numbers_sum = []

for idx in range((len(numbers) // 2)):
    numbers_sum.append(numbers_lst[idx] + sub_list[idx])

print(*numbers_sum, sep=' ')
