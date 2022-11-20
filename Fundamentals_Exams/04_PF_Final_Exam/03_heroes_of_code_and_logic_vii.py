def cast_spell(data):
    """
    This function reduce MP points of current hero. Both scenarios are:
    1. If the hero has the required MP, he casts the spell, thus reducing his MP and returns message.
    2. If the hero is unable to cast the spell returns other massage
    :param data: str
    :return: str
    """
    global heroes
    name = data[1]
    mp_needed = int(data[2])
    spell_name = data[3]
    hero_current_mp = heroes[name][1]
    if hero_current_mp >= mp_needed:
        heroes[name][1] -= mp_needed
        return f'{name} has successfully cast {spell_name} and now has {heroes[name][1]} MP!'
    return f'{name} does not have enough MP to cast {spell_name}!'


def take_damage(data):
    """
    This function reduce HP points of current hero. Both scenarios are:
    1. Reduce the hero HP by the given damage amount. If the hero is still alive (his HP is greater than 0)
    returns message.
    2. If the hero has died, remove him from your party and returns other message.
    :param data: str
    :return: str
    """
    global heroes
    name = data[1]
    damage = int(data[2])
    attacker = data[3]
    heroes[name][0] -= damage
    if heroes[name][0] > 0:
        return f'{name} was hit for {damage} HP by {attacker} and now has {heroes[name][0]} HP left!'
    else:
        del heroes[name]
        return f'{name} has been killed by {attacker}!'


def recharge(data):
    """
    This function increases MP points of current hero.
    :param data: str
    :return: str
    """
    global heroes
    name = data[1]
    amount_mp = int(data[2])
    diff_mp = 200 - heroes[name][1]

    if (heroes[name][1] + amount_mp) > 200:
        heroes[name][1] = 200
        return f'{name} recharged for {diff_mp} MP!'
    else:
        heroes[name][1] += amount_mp
        return f'{name} recharged for {amount_mp} MP!'


def heal(data):
    """
    This function increases HP points of current hero.
    :param data: str
    :return: str
    """
    global heroes
    name = data[1]
    amount_hp = int(data[2])
    diff_hp = 100 - heroes[name][0]

    if (heroes[name][0] + amount_hp) > 100:
        heroes[name][0] = 100
        return f'{name} healed for {diff_hp} HP!'
    else:
        heroes[name][0] += amount_hp
        return f'{name} healed for {amount_hp} HP!'


def output():
    """
    This function prints each hero from heroes dict with his HP and MP points
    """
    global heroes
    for hero, stats in heroes.items():
        print(hero)
        print(f' HP: {stats[0]}')
        print(f' MP: {stats[1]}')


def read_heroes_info():
    """
    This function reads input from console and store data in heroes dict.
    """
    global heroes
    for _ in range(number_of_heroes):
        hero_name, hero_hp, hero_mp = input().split()
        heroes[hero_name] = [int(hero_hp), int(hero_mp)]


number_of_heroes = int(input())

heroes = {}

read_heroes_info()

while True:
    command = input()
    if command == 'End':
        break

    event_data = command.split(' - ')
    event = event_data[0]

    if event == 'CastSpell':
        print(cast_spell(event_data))
    elif event == 'TakeDamage':
        print(take_damage(event_data))
    elif event == 'Recharge':
        print(recharge(event_data))
    elif event == 'Heal':
        print(heal(event_data))

output()
