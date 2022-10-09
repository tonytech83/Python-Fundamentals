def trib(number):
    tribonacci_sequence = [1]
    for num in range(1, number):
        if len(tribonacci_sequence) < 3:
            tribonacci_sequence.append(num)
        else:
            tribonacci_sequence.append(sum(tribonacci_sequence[-3:]))

    return tribonacci_sequence


positive_integer = int(input())

print(*trib(positive_integer), sep=' ')
