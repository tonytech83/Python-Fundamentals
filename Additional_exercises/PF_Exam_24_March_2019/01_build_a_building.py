needed_budget = float(input())
initial_capital = float(input())
investors_count = int(input())

collected_money = initial_capital

start_building = False

for investor_idx in range(1, investors_count + 1):
    investor_money = float(input())
    collected_money += investor_money
    print(f'Investor {investor_idx} gave us {investor_money:.2f}.')
    if collected_money >= needed_budget:
        start_building = True
        break

if start_building:
    print(f'We will manage to build it. Start now! Extra money - {(collected_money - needed_budget):.2f}.')
else:
    print(f'Project can not start. We need {(needed_budget - collected_money):.2f} more.')
