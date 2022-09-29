animal = []

for _ in range(3):
    current_string = input()
    animal.append(current_string)

animal[0], animal[2] = animal[2], animal[0]

print(animal)
