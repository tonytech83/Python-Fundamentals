number = int(input())

# Shift the number n times to the right (where n is the position, in this case, it is 1) by using the >> operator.
# In that way, the bit we want to check will be at position 0;
number_to_binary = bin(number >> 1)

# Find and print the bit at position 0
print(number_to_binary[-1])
