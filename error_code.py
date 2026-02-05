# This file has errors that need to be fixed
# Use what you know about Python to fix them

import random
from error_code_function import combat, create_monster  

char_name = input("Please enter a character name:\n")
char_class = 0
items = ["sword","shield","potion","spyglass","wand","dagger","spellbook","coinpurse"]
items = [] 
class_stats = {
    "Fighter":{
        "health":100,
        "attack":50,
        "defense":75,
        "damage":25,
        "gold": 0,
        "luck":20,
        "inventory":[]
        },
    "Wizard":{
        "health":25,
        "attack":75,
        "defense":50,
        "damage":100,
        "gold":0,
        "luck":50,
        "inventory":[]
        },
    "Rogue":{
        "health":50,
        "attack":25,
        "defense":100,
        "damage":75,
        "gold":0,
        "luck":80,
        "inventory":[]
        }
}


while char_class < 1 and char_class > 3:
    try:
        char_class = input("Please pick a character class:\n1. Fighter\n2. Wizard\n3. Rogue\n")
        char_class = int(char_class)
    except TypeError: 
        print("Invalid Choice\n")

if char_class == 1:
    char_class = class_stats["Fighter"]
elif char_class == 2:
    char_class = class_stats["Wizard"]
else:
    char_class = class_stats["Rogue"]

char_class["name"] = char_name   
print("\n========================================")
print(f"Welcome, {char_class['name']}!")
print(f"Starting Stats -> HP: {char_class['health']} | ATK: {char_class['attack']} | DEF: {char_class['defense']} | DMG: {char_class['damage']} | LUCK: {char_class['luck']} | GOLD: {char_class['gold']}")
print("========================================\n")

FIRST_PASS = True
while True:
    if not FIRST_PASS:
        print(f"\nSTATUS -> HP: {char_class['health']} | GOLD: {char_class['gold']} | INVENTORY: {len(char_class['inventory'])} item(s)")

    choice = input("What would you like to do?:\n1.Combat\n2.Search\n3.Flee\n").lower()
    if choice == "Combat" or choice == "1":
        monster = create_monster()
        print("\nA monster lurches out of the darkness...")
        print(f"ENEMY STATS -> HP: {monster['health']} | ATK: {monster['attack']} | DEF: {monster['defense']} | DMG: {monster['damage']}")
        print("Prepare for combat!\n")
        rounds = 0
        MAX_ROUNDS = 25
        while monster["health"] > 0 and char_class["health"] > 0:
            rounds += 1

            
            char_class, monster = combat(monster, char_class)

            print(f"COMBAT UPDATE -> You: {char_class['health']} HP | Monster: {monster['health']} HP")

            if rounds >= MAX_ROUNDS:
                break

        if rounds >= MAX_ROUNDS:
                print("\nThe fight drags on... neither side can land a clean hit.")
                print("You break away and retreat before this becomes your whole personality.")
        elif monster["health"] > 0:
            print(f"You were slain by the {monster[char]}!") 
            print("Your vision fades. The dungeon claims another hero.")
            break
        else:
            gold = random.randint(
                min(monster["attack"],monster["damage"]),
                max(monster["attack"],monster["damage"])
                )
            print(f"You were victorious! You gain {gold} gold!")
        
            char_class = char_class["gold"] + gold

            print(f"TOTAL GOLD: {char_class['gold']}") 

    elif choice == "Search" or choice == "2":
        did_find = random.randint(1,100)

        if did_find < char_class["Luck"]:
            found_item = random.choice(items) 
            char_class["inventory"].append(found_item)
            print(f"You search the area... and find a {found_item}!")
            print(f"Inventory: {char_class['inventory']}")
        else:
            print("You search the area... nothing but dust and disappointment.")

    elif choice == "Flee" or choice == "3":
        print("You run. Very brave. Extremely tactical.")
        print("Sometimes living is winning.")
        break
    else:
        print("Please choose a valid option.")
    print("========================================")

    FIRST_PASS == False

print(f"Final Stats -> HP: {char_class['health']} | GOLD: {char_class['gold']} | INVENTORY: {char_class['inventory']}")
print("Goodbye!")
