lost_battles = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_broken = lost_battles // 2
sword_broken = lost_battles // 3
shield_broken = lost_battles // 6
armor_broken = shield_broken // 2

repair_expenses = helmet_broken * helmet_price + sword_broken * sword_price + \
                  shield_broken * shield_price + armor_broken * armor_price

print(f'Gladiator expenses: {repair_expenses:.2f} aureus')
