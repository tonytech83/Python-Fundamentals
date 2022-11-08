def character_multiplier(str1, str2, current_diff):
    global total_sum
    for idx in range(len(str1)):
        total_sum += ord(str1[idx]) * ord(str2[idx])
    for char in current_diff:
        total_sum += ord(char)


string_one, string_two = input().split()
total_sum = 0

if len(string_one) > len(string_two):
    diff = string_one[len(string_two):]
    character_multiplier(string_two, string_one, diff)
else:
    diff = string_two[len(string_one):]
    character_multiplier(string_one, string_two, diff)

print(total_sum)
