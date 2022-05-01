"""
This program is to make pancakes
"""
print("Lets make Traditional Pancakes!")
print("Serves 6")
print("")
batch_quantity = (int(input("How many batches would you like to make? ")))
print("")
print("Ingredients:")
milk = 1 * batch_quantity
eggs = 1 * batch_quantity
butter = 30 * batch_quantity
flour = 1 * batch_quantity
sugar = 2 * batch_quantity
print(milk, "cups of Meadow Fresh Original Milk")
print(eggs, "egg lightly beaten")
print(butter, "g of Tararua Butter")
print(flour, "cup of Edmonds Self Raising Flour")
print(sugar, "Tbsp Chelsea White Sugar")
print("")
FLOUR_2 = "Edmonds Self Raising Flour"
SUGAR_2 = "Chelsea White Sugar"
MILK_2 = "Meadow Fresh Original Milk"
EGGS_2 = "egg"
BUTTER_2 = "melted Tararua Butter"
BUTTER_3 = "Tararua Butter"
dry_ingredients = f"Sift the  {FLOUR_2} and {SUGAR_2} into a bowl."
wet_ingredients = f"Add  {MILK_2}, {EGGS_2} and {BUTTER_2} and whisk to combine."
print("Instructions:")
print(dry_ingredients)
print("Make a well in the centre of the dry ingredients.")
print(wet_ingredients)
print("Heat a large non stick frying pan over medium low heat and grease lightly with {BUTTER_3}.")
print("For each pancake, place 2 tablespoons of batter into the pan.")
print("Cook until bubbles burst on surface and the edges start to go dry.")
print("Turn and cook other side until golden brown.")
