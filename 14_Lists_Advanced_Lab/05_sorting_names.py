names_list = input().split(', ')
sorted_list = sorted(names_list, key=lambda name: (-len(name), name))

print(sorted_list)
