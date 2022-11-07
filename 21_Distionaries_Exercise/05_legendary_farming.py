def check_key_materials(all_materials):
    global legendary_item
    if all_materials['shards'] >= 250:
        materials['shards'] -= 250
        legendary_item = 'Shadowmourne'
        return True
    elif all_materials['fragments'] >= 250:
        materials['fragments'] -= 250
        legendary_item = 'Valanyr'
        return True
    elif all_materials['motes'] >= 250:
        materials['motes'] -= 250
        legendary_item = 'Dragonwrath'
        return True
    else:
        return False


materials = {"shards": 0,
             "fragments": 0,
             "motes": 0
             }

legendary_item = None

while True:
    line = input().split()

    for idx in range(0, len(line), 2):
        material = line[idx + 1].lower()
        quantity = int(line[idx])

        if material not in materials:
            materials[material] = quantity
        else:
            materials[material] += quantity
        if check_key_materials(materials):
            break
    if legendary_item is not None:
        break

print(f'{legendary_item} obtained!')

for key, value in materials.items():
    print(f'{key}: {value}')
