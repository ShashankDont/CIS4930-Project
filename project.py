# Read Ingredients CSV
def read_ingredients(file_path):
    ingredients = {}
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            ingredients[row['ingredient_name']] = {
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

# Main Function
def main():
    # Read data from files
    available_ingredients = read_ingredients(INGREDIENTS_CSV)
    user_prefs = read_user_preferences(USER_PREFS_FILE)
    

if __name__ == "__main__":
    main()
