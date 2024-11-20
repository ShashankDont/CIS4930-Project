import csv
import json
import yaml
import random
import matplotlib.pyplot as plt


recipes = {
    "Pasta": {"ingredients" : {"pasta" : 100, "tomato" : 50}, "diet" : "vegetarian"},
    "Chicken salad" : {"ingredients" : {"chicken" : 150, "lettuce" : 50, "tomato" : 50, "cucumber" : 20, "avocado" : 30}, "diet" : "high-protein"},
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
    "chicken stir-fry" : {"ingredients" : {"chicken" : 150, "bell pepper" : 50, "carrot" : 30, "soy sauce" : 15}, "diet" : "high-protein"},
    "grilled salmon" : {"ingredients" : {"salmon" : 200, "lemon" : 1, "olive oil" : 10}, "diet" : "high-protein"},
    "beef taco bowl" : {"ingredients" : {"rice" : 200, "ground beef" : 100, "lettuce" : 30, "cheese" : 20, "salsa" : 15}, "diet" : "high-protein"},
    "chicken caesar salad" : {"ingredients" : {"chicken" : 100, "lettuce" : 50, "croutons" : 20, "parmesan cheese" : 15, "Caesar dressing" : 10}, "diet" : "high-protein"},
    "shrimp pasta" : {"ingredients" : {"pasta" : 100, "shrimp" : 100, "garlic" : 10, "olive oil" : 10}, "diet" : "high-protein"},
    "overnight oats" : {"ingredients" : {"oats" : 50, "almond milk" : 100, "banana" : 1, "chia seeds" : 10}, "diet" : "vegan"},
    "quinoa salad" : {"ingredients" : {"quinoa" : 100, "chickpeas" : 50, "bell pepper" : 20, "cucumber" : 20, "olive oil" : 10}, "diet" : "vegan"},
    "turkey sandwich" : {"ingredients" : {"bread" : 2, "turkey breast" : 50, "lettuce" : 10, "tomato" : 10, "mustard" : 5}, "diet" : "low-carb"},
    "Egg Muffins": {"ingredients" : {'eggs' : 6, 'spinach' : 1, 'cherry tomatoes' : 120, 'cheece' : 130}, "diet" : "low-carb"},
    "Zucchini Noodles" : {"ingredients" : {'zucchini' : 2, 'shrimp' : 340, 'garlic' : 3, 'olive oil' : 30, 'butter' : 30, 'parmesan cheese' : 85}, "diet" : "low-carb"},
    "Avocado Deviled Eggs" : {"ingredients" : {'eggs' : 6, 'avocado' : 1, 'lime juice' : 15, 'garlic powder' : 7.5, 'paprika' : 1.5}, "diet" : "low-carb"},
    "Cauliflower Fried Rice" : {"ingredients" : {'cauliflower rice' : 400, 'eggs' : 100, 'carrots' : 60, 'peas' : 60, 'soy sauce' : 30, 'green onions' : 20, 'garlic' : 6, 'sesame oil' : 14, 'olive oil' : 14}, "diet" : "low-carb"}
}

recipe_nutrition = {
    "Pasta": {'calories': 300, 'protein': 10, 'carbs': 50, 'fat': 5, 'fiber': 3},
    "Chicken Salad": {'calories': 400, 'protein': 25, 'carbs': 10, 'fat': 20, 'fiber': 5},
    "fruit smoothie": {'calories': 200, 'protein': 5, 'carbs': 20, 'fat': 15, 'fiber': 15},
    "oatmeal": {'calories': 150, 'protein': 15, 'carbs': 20, 'fat': 10, 'fiber': 20},
    "Lentil Soup": {'calories': 400, 'protein': 25, 'carbs': 10, 'fat': 20, 'fiber': 5},
    "vegetable stir-fry": {'calories': 250, 'protein': 8, 'carbs': 35, 'fat': 10, 'fiber': 8},
    "greek salad": {'calories': 220, 'protein': 8, 'carbs': 12, 'fat': 15, 'fiber': 4},
    "vegetable omelette": {'calories': 300, 'protein': 18, 'carbs': 5, 'fat': 22, 'fiber': 2},
    "avocado toast": {'calories': 280, 'protein': 6, 'carbs': 30, 'fat': 16, 'fiber': 7},
    "banana pancakes": {'calories': 350, 'protein': 9, 'carbs': 60, 'fat': 10, 'fiber': 4},
    "chickpea salad": {'calories': 200, 'protein': 8, 'carbs': 25, 'fat': 8, 'fiber': 6},
    "vegan burrito": {'calories': 400, 'protein': 12, 'carbs': 55, 'fat': 15, 'fiber': 10},
    "roasted sweet potatoes": {'calories': 180, 'protein': 2, 'carbs': 40, 'fat': 5, 'fiber': 7},
    "chicken stir-fry": {'calories': 350, 'protein': 25, 'carbs': 20, 'fat': 15, 'fiber': 5},
    "grilled salmon": {'calories': 300, 'protein': 35, 'carbs': 0, 'fat': 20, 'fiber': 0},
    "beef taco bowl": {'calories': 500, 'protein': 30, 'carbs': 60, 'fat': 20, 'fiber': 8},
    "chicken caesar salad": {'calories': 400, 'protein': 28, 'carbs': 15, 'fat': 20, 'fiber': 3},
    "shrimp pasta": {'calories': 400, 'protein': 25, 'carbs': 50, 'fat': 15, 'fiber': 3},
    "overnight oats": {'calories': 250, 'protein': 8, 'carbs': 35, 'fat': 8, 'fiber': 10},
    "quinoa salad": {'calories': 300, 'protein': 10, 'carbs': 40, 'fat': 10, 'fiber': 7},
    "turkey sandwich": {'calories': 350, 'protein': 20, 'carbs': 30, 'fat': 15, 'fiber': 3},
    "Egg Muffins": {'calories' : 150, 'protein' : 12, 'carbs' : 2, 'fat' : 10, 'fiber' : 2},
    "Zucchini Noodles" : {"ingredients" : {'calories' : 250, 'protein' : 20, 'carbs' : 5, 'fat' : 15, 'fiber' : 2.5},
    "Avocado Deviled Eggs" : {'calories' : 90, 'protein' : 6, 'carbs' : 1, 'fat' : 7, 'fiber' : 9},
    "Cauliflower Fried Rice" : {'calories' : 200 , 'protein' :10 , 'carbs' : 7, 'fat' : 12, 'fiber' : 14}
}

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
    recommended_recipes = []
    
    # If the diet of the user prefrence and recipe match add it to dict
    for recipe, details in recipes.items():
        if details["diet"] == preferences["diet"]:
            recommended_recipes.append(recipe)
    return recommended_recipes

# Create a meal plan for the week
def create_meal_plan(recommended_recipes):
    # Choose a random recipe for each day from reccomened_recipes dict
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    meal_plan = {day: random.choice(recommended_recipes) for day in days}
    return meal_plan

# Generate a shopping list based on selected recipes and available ingredients
def generate_shopping_list(meal_recipes, ingredients): 
    shopping_list = {}

    # Go through each recipe in each day
    for day, recipe_name in meal_recipes.items():
        recipe_ingredients = recipes[recipe_name]["ingredients"]
        
        # Go through each ingrident in the recipe
        for item, required_qty in recipe_ingredients.items():
            unit = ingredients.get(item, {}).get("unit", "units") # Get the unit of ingredient 
            
            # If ingridient already in shopping list set the avaiable to 0 
            # Else get the amount from starting ingredients
            if item in shopping_list:
                available_qty = 0
            else:
                available_qty = ingredients.get(item, {}).get("quantity", 0)
            
            # If avaiable ingridients less then starting add to list
            if available_qty < required_qty:    
                needed_qty = required_qty - available_qty
                if item in shopping_list:
                    shopping_list[item]["quantity"] += needed_qty
                else:
                    shopping_list[item] = {"quantity": needed_qty, "unit": unit}
            # If avabile ingridents equal to require add ingredient to list with 0 
            elif available_qty == required_qty:
                if item not in shopping_list:
                    shopping_list[item] = {"quantity": 0, "unit": unit}
    
    # Check and remove any ingredients in list with 0 quantity
    shopping_list = {item: details for item, details in shopping_list.items() if details["quantity"] > 0}
    return shopping_list


# Analyze nutrition based on the meal plan and print results
def analyze_nutrition(meal_plan, preferences):
    nutrition_summary = {'total': {}, 'daily': {}, 'comparison': {}}

    # Print out the nutrional values of prefered diet
    print("User's Nutritional Preferences:")
    for nutrient, goal_value in preferences['nutritional_goals'].items():
        print(f"  {nutrient.capitalize()}: {goal_value} total")

    # Calculate nutritional totals based on the meal plan
    for day, meal in meal_plan.items():
        meal_nutrition = recipe_nutrition.get(meal, {})
        nutrition_summary['daily'][day] = meal_nutrition
        for nutrient, value in meal_nutrition.items():
            nutrition_summary['total'][nutrient] = nutrition_summary['total'].get(nutrient, 0) + value

    # Print out meal plan's nutritional values per day
    print("\nMeal Plan's Nutritional Values Per Day:")
    for day, nutrients in nutrition_summary['daily'].items():
        print(f"  {day}:")
        for nutrient, value in nutrients.items():
            print(f"    {nutrient.capitalize()}: {value}")

    # Calculate and compare total nutritional values against user preferences
    print("\nTotal Nutritional Values for the Meal Plan (average per day):")
    for nutrient, goal_value in preferences['nutritional_goals'].items():
        total_nutrient_value = nutrition_summary['total'].get(nutrient, 0) 
        difference = total_nutrient_value - goal_value

        print(f"  {nutrient.capitalize()}:")
        print(f"    Goal: {goal_value}")
        print(f"    Actual : {total_nutrient_value:.2f}")
        print(f"    Difference: {difference:.2f}")

    return nutrition_summary


# Visualize nutrition data per day
def visualize_nutrition_data(nutrition_summary):
    days = nutrition_summary['daily'].keys()
    nutrients = list(nutrition_summary['total'].keys())
    
    # Create a list of daily values for each nutrient
    daily_values = {nutrient: [] for nutrient in nutrients}
    for day in days:
        for nutrient in nutrients:
            daily_values[nutrient].append(nutrition_summary['daily'].get(day, {}).get(nutrient, 0))

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    bar_width = 0.1
    x = list(range(len(days)))
    
    for i, nutrient in enumerate(nutrients):
        ax.bar(
            [p + bar_width * i for p in x],
            daily_values[nutrient],
            width=bar_width,
            label=nutrient
        )

    ax.set_xticks([p + bar_width * (len(nutrients) / 2) for p in x])
    ax.set_xticklabels(days)
    ax.set_xlabel("Days")
    ax.set_ylabel("Nutrient Amount")
    ax.set_title("Daily Nutritional Intake")
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Main Function
def main():
    ingredients_file = 'ingredients.csv'  
    preferences_file = 'preferences.json'

    available_ingredients = read_ingredients(ingredients_file)
    user_prefs = read_user_preferences(preferences_file)   
    
    # User input of their prefered diet from 4 options
    while True:
        try:
            preference_input = int(input("Enter a number 1-4 (1: Vegetarian  2: Vegan  3: High Protein  4: Low Carb): "))
            if 1 <= preference_input <= 4:
                break
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number between 1 and 4.")
            
    preference_input -= 1
    
    # Calls the functions to create meal plan and shopping list
    recommended_recipes = recommend_recipes(available_ingredients, user_prefs["user_preferences"][preference_input])
    meal_plan = create_meal_plan(recommended_recipes)
    shopping_list = generate_shopping_list(meal_plan, available_ingredients)
    nutrition_summary = analyze_nutrition(meal_plan, user_prefs["user_preferences"][preference_input])

    # Writes meal plan and shopping list to a file
    with open('meal_plan.txt', 'w') as file:
        file.write("Weekly Meal Plan:\n")
        for day, meal in meal_plan.items():
            file.write(f"{day}: {meal}\n")
        file.write("\nShopping List:\n")
        for item, details in shopping_list.items():
            quantity = details["quantity"]
            unit = details["unit"]
            file.write(f"{item} - {quantity} {unit}\n")


    visualize_nutrition_data(nutrition_summary)

if __name__ == "__main__":
    main()
