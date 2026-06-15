# ==============================================================================
# PROJECT : Mythic Blacksmith Forge Simulator
# AUTHOR  : SIMON NYOKABI
# DESCRIPTION: A modular console application simulating an inventory manager,
#              merchant trading system, and a multi-resource crafting engine.
# ==============================================================================
# KEY LEARNINGS & DEBUGGING BREAKTHROUGHS FROM THE MISTAKES i MADE:
#
# 1. Variable Scope & Reusability: Decoupled functions from global variables 
#    by utilizing parameters (e.g., inventory_dict). The code is now modular 
#    and functions can evaluate any inventory data structure passed to them.
#
# 2. The "Flag" Pattern Where some items needed more than 1 resource: I solved a critical "Loop Trap" 
#    where resources were deducted prematurely before checking all requirements. 
#    Implemented a two-pass "can_craft" boolean flag check to ensure inventory 
#    is only mutated if *all* conditions pass.
#
# 3. AVOIDING FREE GOLD (LOL): I maastered return values to pass updated immutable data 
#    (shop_gold) back to the main game loop, preventing data desynchronization 
#    and infinite gold exploits.
#
# 4. Input Robustness: I opted for string-literal menu handling (choice == "1") 
#    instead of strict integer casting (int(input())). This structurally protects 
#    the application from crashing if a user accidentally enters text or hits Enter.
# ==============================================================================
# The starter inventory data structure
forge_inventory = {
    "Iron Ore": {"quantity": 15, "value": 10},
    "Gold Nugget": {"quantity": 3, "value": 50},
    "Dragon Scale": {"quantity": 1, "value": 150},
}

# The crafting recipes (What items require which materials)
recipes = {
    "Iron Sword": {"Iron Ore": 3},
    "Golden Shield": {"Gold Nugget": 2, "Iron Ore": 1},
    "Dragon Armor": {"Dragon Scale": 1, "Gold Nugget": 1, "Iron Ore": 5}
}

shop_gold = 100

#Write a function to oop through the forge_inventory and print each item, how many are in stock, and its individual value.
def show_inventory(inventory_dict, gold_count):
    for material, details in inventory_dict.items():
        print(f"Material: {material}*** Amount: {details['quantity']}*** Cost: {details['value']}")
    print(f"Remaining Gold: {gold_count}")
    return gold_count

#Prompting the user(Shop owner) to enter the name, quantity  of a material they want to buy from a traveling merchant and Calculate the total cost.
def buy_material(inventory_dict, gold_count):
    material_name = input("What do you want to buy (1. Iron Ore 2. Gold Nugget 3.Dragon Scale ): ")
    required_amount = int(input(f"How much {material_name} do you want to buy? : "))
    
    
    if material_name in inventory_dict:
        material_cost = inventory_dict[material_name]['value']
    else:
         print("***The material is new to the store***")
         material_cost = int(input(f"What is the value of {material_name} per unit?  : "))
         inventory_dict[material_name] = {"quantity":0 , "value": material_cost}           
    total_cost = material_cost * required_amount      
    if gold_count < total_cost:
        print(f"No enough Gold! Remaining amount: {gold_count}")
        if inventory_dict[material_name]['quantity']==0 : # they cant afford
            del inventory_dict[material_name] #remove the material oh no !
    else:
        gold_count -= total_cost
        inventory_dict[material_name]['quantity'] += required_amount
        print(f"Used {total_cost} Golds! Remaining amount: {gold_count}") 
    print(show_inventory(inventory_dict, gold_count))
    return gold_count

#The Grand Forge NestedlLoops & Crafting logic
def craft_item(recipes_dict , inventory_dict):
    item_name = input("What would you like to forge ? :")

    #checking if we have its recipe
    if item_name in recipes_dict:
        item_requirements = recipes_dict[item_name] 
        can_craft = True    
        for material, needed_amount in item_requirements.items():
            if material not in inventory_dict or needed_amount > inventory_dict[material]['quantity']:
                can_craft = False
                print(f"You do not have enough {material}")
        if can_craft:
            for material, needed_amount in item_requirements.items():
                inventory_dict[material]['quantity']-= needed_amount
                print(f"Used {needed_amount} {material}--- Remaining amount: {inventory_dict[material]['quantity']}")        
            print(f"{item_name} Crafted Succesfully !!!")                                 
    else:
        print(f"{item_name}'s recipe is unavailable")

# THE MENU
while True:
    print("--- MYTHIC BLACKSMITH FORGE ---")
    print("1. View Shop Inventory\n" \
    "2. Buy Materials from Merchant\n" \
    "3. Craft Mythic Gear\n" \
    "4. Close Shop (Exit)")
    choice = input("\nWhat would you like to do?: ")
    if choice == "1":
        show_inventory(forge_inventory, shop_gold)
    elif choice == "2":
        shop_gold = buy_material(forge_inventory, shop_gold)
    elif choice== "3":
        craft_item(recipes, forge_inventory)
    elif choice == "4":
        print("Exiting the Workspace !!!")
        break
    else:
        print("Invalid choice! Kindly select Option 1-4")
    