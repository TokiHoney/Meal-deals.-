import requests
import json

def fetch_meals_by_category(category):
    url = f'https://www.themealdb.com/api/json/v1/1/filter.php?c={category}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('meals', [])
    return []

def build_menu():
    categories_map = {
        'Appetizer': 'Starter',
        'Entree': 'Beef',
        'Dessert': 'Dessert',
        'Drink': 'Side'  # Sides used as placeholder for drinks
    }

    menu = {}
    for menu_cat, api_cat in categories_map.items():
        meals = fetch_meals_by_category(api_cat)
        items = []
        for idx, meal in enumerate(meals[:25]):  # 25 per category to start
            item = {
                'name': meal['strMeal'],
                'price': (idx % 5) + 1,
                'source': 'Homemade' if idx % 2 == 0 else 'Fast Food',
                'img': meal['strMealThumb']
            }
            items.append(item)
        menu[menu_cat] = items

    with open('Menu.json', 'w') as f:
        json.dump(menu, f, indent=2)
    print("Menu.json created with sample meals.")

if __name__ == '__main__':
    build_menu()
