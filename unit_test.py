import unittest
from unittest.mock import patch, mock_open
from project import (
    read_ingredients,
    read_user_preferences,
    recommend_recipes,
    create_meal_plan,
    generate_shopping_list,
    analyze_nutrition
)

class TestMealPlanner(unittest.TestCase):

    def setUp(self):
        # Sample data for testing
        self.sample_ingredients_csv = "name,quantity,unit\npasta,100,grams\ntomato,50,grams\n"
        self.sample_user_preferences_json = '{"user_preferences": [{"diet": "vegetarian", "nutritional_goals": {"calories": 2000, "protein": 50, "carbs": 250, "fat": 70}}]}'

        self.sample_ingredients_dict = {
            'pasta': {'quantity': 100, 'unit': 'grams'},
            'tomato': {'quantity': 50, 'unit': 'grams'}
        }
        self.sample_user_preferences = {
            "user_preferences": [{"diet": "vegetarian", "nutritional_goals": {"calories": 2000, "protein": 50, "carbs": 250, "fat": 70}}]
        }
        self.sample_recommended_recipes = ["Pasta", "fruit smoothie"]

    def test_read_ingredients(self):
        with patch('builtins.open', mock_open(read_data=self.sample_ingredients_csv)):
            ingredients = read_ingredients('ingredients.csv')
            self.assertEqual(ingredients, self.sample_ingredients_dict)

    def test_read_user_preferences_json(self):
        with patch('builtins.open', mock_open(read_data=self.sample_user_preferences_json)):
            preferences = read_user_preferences('preferences.json')
            self.assertEqual(preferences, self.sample_user_preferences)

    def test_recommend_recipes(self):
        recommended = recommend_recipes(self.sample_ingredients_dict, self.sample_user_preferences["user_preferences"][0])
        self.assertIn("Pasta", recommended)

    def test_create_meal_plan(self):
        meal_plan = create_meal_plan(self.sample_recommended_recipes)
        self.assertEqual(len(meal_plan), 7)

    def test_generate_shopping_list(self):
        meal_recipes = {
            "Monday": "Pasta",
            "Tuesday": "Pasta"
        }
        shopping_list = generate_shopping_list(meal_recipes, self.sample_ingredients_dict)
        expected_shopping_list = {
            'pasta': {'quantity': 100, 'unit': 'grams'},
            'tomato': {'quantity': 50, 'unit': 'grams'}
        }
        self.assertEqual(shopping_list, expected_shopping_list)

    def test_analyze_nutrition(self):
        meal_plan = {
            "Monday": "Pasta",
            "Tuesday": "Pasta"
            
        }
        preferences = {"diet": "vegetarian", "nutritional_goals": {"calories": 2000, "protein": 50, "carbs": 250, "fat": 70}}
        nutrition_summary = analyze_nutrition(meal_plan, preferences)
        self.assertIn("total", nutrition_summary)
        self.assertIn("calories", nutrition_summary["total"])

if __name__ == '__main__':
    unittest.main()
