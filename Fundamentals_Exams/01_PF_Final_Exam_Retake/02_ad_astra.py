import re


def days_left(data):
    global total_calories
    global pattern

    extracted_calories = re.finditer(pattern, data)

    for item_calories in extracted_calories:
        calories = item_calories.group(4)
        total_calories += int(calories)

    days = total_calories // 2000
    print(f'You have food to last you for: {days} days!')


def extract_food_info(data):
    global total_calories
    global pattern

    extracted_food = re.finditer(pattern, data)

    for info in extracted_food:
        item_name = info.group(2)
        expiration_date = info.group(3)
        calories = info.group(4)
        print(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}")


text_string = input()
total_calories = 0
pattern = r'([\|#])([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1'

days_left(text_string)
extract_food_info(text_string)
