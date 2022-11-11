number = int(input())
position = int(input())

# Shift the number p times to the right (where n is the position) by using the >> operator.
# In that way, the bit we want to check will be at position 0;
number_to_binary = bin(number >> position)

# Find and print the bit at position 0
print(number_to_binary[-1])
