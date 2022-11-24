list_of_times = [x for x in input().split()]

sorted_lst = sorted(list_of_times, reverse=False)

print(*sorted_lst, sep=', ')
