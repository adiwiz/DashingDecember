def get_recipe(ingredients):
    recipes = {
        "Potato Tomato Curry": ["potato", "tomato", "onion", "garlic", "coriander", "chillies", "salt", "turmeric"],
        "Potato Salad": ["potato", "onion", "coriander", "salt", "pepper"],
        "Tomato Garlic Soup": ["tomato", "garlic", "onion", "salt", "pepper"],
        "Spicy Potato Stir-Fry": ["potato", "onion", "garlic", "chillies", "salt", "turmeric"],
        "Tomato Coriander Chutney": ["tomato", "coriander", "garlic", "chillies", "salt"]
    }

    suggested_recipes = []

    for recipe, required_ingredients in recipes.items():
        if all(item in ingredients for item in required_ingredients):
            suggested_recipes.append(recipe)

    if suggested_recipes:
        return f"Based on your ingredients, you can make: {', '.join(suggested_recipes)}"
    else:
        return "Sorry, no recipes found for the given ingredients."

if __name__ == "__main__":
    user_ingredients = input("Enter the ingredients you have, separated by commas: ").lower().split(", ")
    print(get_recipe(user_ingredients))
