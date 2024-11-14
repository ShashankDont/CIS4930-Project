import csv
import json
import yaml
import random
import matplotlib.pyplot as plt

# Read Ingredients CSV
def read_ingredients(file_path):
    ingredients = {}
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            ingredients[row['name'].lower()] = {
                'quantity': float(row['quantity']),
                'unit': row['unit']
            }
    return ingredients

# Read User Preferences (JSON or YAML)
def read_user_preferences(file_path):
    with open(file_path, mode='r') as file:
        if file_path.endswith('.json'):
            return json.load(file)
        elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
            return yaml.safe_load(file)
        else:
            raise ValueError('Unsupported file format. Use JSON or YAML.')
        
# Suggest meals based on available ingredients and user preferences
def recommend_recipes(ingredients, preferences):
    recipes = {
        "Pasta": {"ingredients" : {"pasta" : 100, "tomato" : 50}, "diet" : "vegetarian"},
        "Chicken salad" : {"ingredients" : {"chicke" : 150, "lettuce" : 50, "tomato" : 50, "cucumber" : 20, "avocado" : 30}, "diet" : "non-vegetarian"},
        "fruit smoothie" : {"ingredients" : {"banana" : 1, "milk" : 200, "strawberries" : 50, "blueberries" : 30}, "diet" : "vegetarian"},
        "oatmeal" : {"ingredients" : {"oats" : 100, "milk" : 200}, "diet" : "vegan"},
        "Lentil soup" : {"ingredients" : {"lentils" : 100, "carrot" : 2, "spinach" : 50}, "diet" : "vegan"},
        "vegetable stir-fry" : {"ingredients" : {"bell pepper" : 100, "carrot" : 50, "broccoli" : 100, "soy sauce" : 15}, "diet" : "vegetarian"},
        "greek salad" : {"ingredients" : {"lettuce" : 50, "tomato" : 30, "cucumber" : 30, "feta cheese" : 50, "olive oil" : 10}, "diet" : "vegetarian"},
        "vegetable omelette" : {"ingredients" : {"egg" : 2, "bell pepper" : 20, "tomato" :20, "spinach" : 20, "cheese" : 15}, "diet" : "vegetarian"},
        "avocado toast" : {"ingredients" : {"bread" : 1, "avocado" : 50, "tomato" : 20}, "diet" : "vegetarian"},
        "banana pancakes" : {"ingredients" : {"banana" : 1, "flour" : 50, "milk" : 100, "egg" : 1}, "diet" : "vegetarian"},
        "chickpea salad" : {"ingredients" : {"chickpeas" : 100, "cucumber" : 50, "tomato" : 30, "olive oil" : 10}, "diet" : "vegan"},
        "vegan burrito" : {"ingredients" : {"tortilla" : 1, "black beans" : 50, "lettuce" : 30, "tomato" : 20, "avocado" : 50}, "diet" : "vegan"},
        "roasted sweet potatoes" : {"ingredients" : {"sweet potato" : 200, "olive oil" : 10, "salt" : 1}, "diet" : "vegan"},
        "chicken stir-fry" : {"ingredients" : {"chicken" : 150, "bell pepper" : 50, "carrot" : 30, "soy sauce" : 15}, "diet" : "non-vegetarian"},
        "grilled salmon" : {"ingredients" : {"salmon" : 200, "lemon" : 1, "olive oil" : 10}, "diet" : "non-vegetarian"},
        "beef taco bowl" : {"ingredients" : {"rice" : 200, "ground beef" : 100, "lettuce" : 30, "cheese" : 20, "salsa" : 15}, "diet" : "non-vegetarian"},
        "chicken caesar salad" : {"ingredients" : {"chicken" : 100, "lettuce" : 50, "croutons" : 20, "parmesan cheese" : 15, "Caesar dressing" : 10}, "diet" : "non-vegetarian"},
        "shrimp pasta" : {"ingredients" : {"pasta" : 100, "shrimp" : 100, "garlic" : 10, "olive oil" : 10}, "diet" : "non-vegetarian"},
        "overnight oats" : {"ingredients" : {"oats" : 50, "almond milk" : 100, "banana" : 1, "chia seeds" : 10}, "diet" : "vegan"},
        "quinoa salad" : {"ingredients" : {"quinoa" : 100, "chickpeas" : 50, "bell pepper" : 20, "cucumber" : 20, "olive oil" : 10}, "diet" : "vegan"},
        "turkey sandwich" : {"ingredients" : {"bread" : 2, "turkey breast" : 50, "lettuce" : 10, "tomato" : 10, "mustard" : 5}, "diet" : "non-vegetarian"}
    }

    recommend_recipes = []
    for recipe, details in recipe.items():
        if details["diet"] == preferences["diet"] and all(
            item in ingredients and ingredients[item]["quantity"] >= quantity
            for item, quantity in details["ingredients"].items()):
                recommended_recipes.append(recipe)
    return recommend_recipes

def create_meal_plan(recommend_recipes):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    meal_plan = {}

    for day in days:
        meal_plan[day] = random.choice(recommended_recipes)

    return meal_plan

def generate_shopping_list(recipes, ingredients): 
    shopping_list = {}

    for recipe in recipes:
        for item, required_qty in recipes[recipe]["ingredients"].items():
            if item in ingredients:
                needed_qty = required_qty - ingredients[item]["quantity"]
                if needed_qty > 0:
                    shopping_list[item] = shopping_list.get(item, 0) + needed_qty
                else:
                    shopping_list[item] = required_qty
    
    return shopping_list

def analyze_nutrition(meal_plan, recipes, preferences, recipe_nutrition):
    nutrition_summary = {'total' : {}, 'daily' : {}, 'per_meal' : {}, 'comparison' : {}}

    for day, meal in meal_plan.items():
        meal_nutrition = recipe_nutrition.get(meal, {})
        nutrition_summary['daily'][day] = meal_nutrition
        for nutrient, value in meal_nutrition.items():
            nutrition_summary['total'][nutrient] = nutrition_summary['total'].get(nutrient, 0) + value

    for nutrient, goal_value in preferences['nutritional_goals'].items():
        actual = nutrition_summary['total'].get(nutrient, 0) / 7
        difference = goal_value - actual
        nutrition_summary['comparison'][nutrient] = {'goal' : goal_value, 'actual' : actual, 'difference' : difference}

    return nutrition_summary

def visualize_nutrition_data(nutrition_summary):
    nutrients = list(nutrition_summary['compaison'].keys())
    goals = [nutrition_summary['comparison'][n]['goal'] for n in nutrients]
    actuals = [nutrition_summary['comparison'][n]['actual'] for n in nutrients]

    fig, ax = plt.subplots()
    ax.bar(nutrients, goals, label="Goal", color = 'blue', alpha = 0.6)
    ax.bar(nutrients, actuals, label="Actual", color = 'red', alpha = 0.7)

    ax.set_xlabel("Nutrients")
    ax.set_ylabel("Amount")
    ax.set_title("Nutritional Goal vs Actual Intake")
    ax.legend()
    plt.show()
 
# Main Function
def main():
    
    ingredients_file = 'ingredients.csv'  
    preferences_file = 'preferences.yml'

    # Read data from files
    available_ingredients = read_ingredients(ingredients_file)
    user_prefs = read_user_preferences(preferences_file)
    
    recommend_recipes = recommend_recipes(available_ingredients, user_prefs["user_preferences"][0])
    meal_plan = create_meal_plan(recommended_recipes)
    shopping_list = generate_shopping_list(recommended_recipes, available_ingredients)
    nutrition_summary = analyze_nutrition(meal_plan, recommended_recipes, user_prefs["user_preferences"][0], {})

    with open('meal_plan.txt', 'w') as file:
        file.write("Weekly Meal Plan: \n")
        for day, meal in meal_plan.items():
            file.write(f"{day}: {meal}\n")

        file.write("\n Shopping List: \n")
        for item, qty in shopping_list.items():
            file.write(f"{item} - {qty}\n")

    visualize_nutrition_data(nutrition_summary)

if __name__ == "__main__":
    main()
