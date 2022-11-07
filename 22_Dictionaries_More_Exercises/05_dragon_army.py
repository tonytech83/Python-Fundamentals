class Dragon:
    def __init__(self, type: str, name: str, damage: int, health: int, armor: int):
        self.type = type
        self.name = name
        self.damage = damage
        self.health = health
        self.armor = armor

    def add_dragon(self):
        if self.type not in dragon_army.keys():
            dragon_army[self.type] = {}
            if self.name not in dragon_army[self.type].keys():
                dragon_army[self.type][self.name] = []
                dragon_army[self.type][self.name].append(self.damage)
                dragon_army[self.type][self.name].append(self.health)
                dragon_army[self.type][self.name].append(self.armor)
            else:
                dragon_army[self.type][self.name][0] = self.damage
                dragon_army[self.type][self.name][1] = self.health
                dragon_army[self.type][self.name][2] = self.armor
        else:
            if self.name not in dragon_army[self.type].keys():
                dragon_army[self.type][self.name] = []
                dragon_army[self.type][self.name].append(self.damage)
                dragon_army[self.type][self.name].append(self.health)
                dragon_army[self.type][self.name].append(self.armor)
            else:
                dragon_army[self.type][self.name][0] = self.damage
                dragon_army[self.type][self.name][1] = self.health
                dragon_army[self.type][self.name][2] = self.armor


dragon_army = {}
dragon_average_stats = {}
number_of_dragons = int(input())

for _ in range(number_of_dragons):
    data = input().split()
    dragon_type = data[0]
    dragon_name = data[1]
    dragon_damage = data[2]
    dragon_health = data[3]
    dragon_armor = data[4]

    if data[2] == 'null':
        dragon_damage = 45
    if data[3] == 'null':
        dragon_health = 250
    if data[4] == 'null':
        dragon_armor = 10

    new_dragon = Dragon(dragon_type, dragon_name, int(dragon_damage), int(dragon_health), int(dragon_armor))
    Dragon.add_dragon(new_dragon)

# calculate average
for color, dragon_info in dragon_army.items():
    total_damage = 0
    total_health = 0
    total_armor = 0
    for dragon_stats in dragon_info.values():
        total_damage += dragon_stats[0]
        total_health += dragon_stats[1]
        total_armor += dragon_stats[2]
    avr_damage = total_damage / len(dragon_info)
    avr_health = total_health / len(dragon_info)
    avr_armor = total_armor / len(dragon_info)

    print(f'{color}::({avr_damage:.2f}/{avr_health:.2f}/{avr_armor:.2f})')
    for name, stats in sorted(dragon_info.items(), key=lambda kvp: kvp[0]):
        print(f'-{name} -> damage: {stats[0]}, health: {stats[1]}, armor: {stats[2]}')
