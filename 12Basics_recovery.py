player_name = 'Simon'
level = 0
health_pct = 0.00
is_online = True
print(f"Status: Player {player_name} is at level {level} with {health_pct}% HP. Online: {is_online}")

if health_pct == 0.0:
    print("Game Over! You are at 0%.")
elif health_pct < 20.0 :
    print('"Warning: Low Health!"')
else:
    print("You are healthy and ready to fight!")

inventory = ["Sword", "Shield", "Bread"]
if 'Bread' in inventory:
    print("You have food!")
    inventory.remove("Bread")
print(inventory)
magic_inventory = []
#
for item in inventory:
    new_item = f'Magic {item}'
    magic_inventory.append(new_item)
print(magic_inventory)

def gain_xp(current_level):
    new_level = current_level + 1
    return new_level
level = gain_xp(level)
print(level)

#PLAYERS INFORMATION
simon_data ={"name":'Simon',
            "level":level,
            "Items":magic_inventory,
            "health_pct":100}
simon_data["level"] = gain_xp(simon_data["level"])
print(simon_data)

#action of thr game 
def take_damage(data_dict):
    data_dict["health_pct"]-= 20
    if data_dict["health_pct"] < 50:
        return "Warning: Health is low!"
    return "Still standing!"
enemies = ["Goblin", "Orc", "Dragon"]
for enemy in enemies:    
    print(take_damage(simon_data))


