# LEARNING RECAP:I Mastered OOP Inheritance & JSON File I/O (to replace the old txt files I was using)
# KEY FIXES: 
# 1. I Tracked local resource updates inside logic blocks (no free items LOL)
# 2. I matched file extensions strictly between writing and loading (.json) was forgetting this part mostly, leaving out the .json.
# 3. I leanrt to always use invocation parentheses () to execute methods, not just reference them (or leaving them to vscode as I did previously)
# 4.Fought this for 10 mins
        # 4. Data flows Right "source" to Left "my target " (=). 
        # To restore states, unpack dictionary keys from the source file into the object's active attributes.
# 5. Inheritance passes down parent behaviors (methods) and baseline attributes, but data values belong strictly to the instance attributes, not the method names.
  # learnt the hard on line 63 and 64 ..oh no
import json
class Forge:
    def __init__(self, player_name):
        self.player = player_name
        self.inventory ={"iron": 5, "gold":0 ,"wood":3}
    def mine_materials(self):
        self.inventory["iron"] +=3
        self.inventory["gold"] +=1
        print("Successfully mined 3 iron and 1 gold")
    def craft_sword(self):
        if self.inventory["iron"] >= 4 and self.inventory["wood"] >= 1:
            self.inventory["iron"] -=4
            self.inventory["wood"] -= 1
            print("Successfully crafted a legendary sword!!!")
        else:
            print("Error: You do not have enough materails. Consider Mining")
    def save_progress(self):
        with open("forge_save.json", "w") as file:
            json.dump(self.inventory,file, indent=4)
            print("Successfuly saved progress")
    def loading_progress(self):
        try:
            with open("forge_save.json", "r") as file:
                loaded_data = json.load(file)
                self.inventory = loaded_data
                print("Successfully loaded the data")
        except FileNotFoundError:
            print("No saved file was found. Refreshing...")

'''print("****Starting session 1 Mining materials and saving****")
player_ses1 =Forge("Simon")
player_ses1.mine_materials()
player_ses1.save_progress()
print("****Starting session 2 Player closing and loging in ****")
player_ses2 = Forge("Simon")
player_ses2.loading_progress()
#I PROVE THAT THE LOADING IS WORKING
print(f"Simon's Loaded Iron as :{player_ses2.inventory["iron"]}")'''

#using inheritance 
class Player:
    def __init__(self, player_name):
        self.name = player_name
        self.mana = 10
    def save_character(self):
        self.character = {"name": self.name, "mana": self.mana}
        with open("character_save.json", "w") as file:
            json.dump(self.character ,file, indent= 4 )
    def load_character(self):
        try:
            with open("character_save.json", "r") as file:
                loaded_char_info = json.load(file)
                self.name = loaded_char_info["name"] 
                self.mana = loaded_char_info["mana"] 
                print("Successfully loaded the character info")
        except FileNotFoundError :
            print("Character data not found. Refreshing...")
class Mage(Player):
    def __init__(self, player_name):
        super().__init__(player_name)
    def cast_spell(self):
        if self.mana >= 3:
            self.mana -= 3
            print("Cast spelled !!!")
        else:
            print(f"No enough mana to cast a spell. Remaining {self.mana}")
#I created an instance for the Mage class( The magcian)
my_mage = Mage("Merlin") # In a land of myth ,..LOL
my_mage.load_character()
my_mage.cast_spell()
my_mage.save_character()

    