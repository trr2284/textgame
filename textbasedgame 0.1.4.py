# this is a very cool rpg game
# Made by trr2284
#
# This game is open source. 
# Modding can be done easily, as finding the extra content you want to add and scripting it in is not difficult if you know python.
#
# For questions on modding, feel free to contact trr2284.
#
# Adding more complex features is more difficult.
#
#

import random
import math
# base stats and loot pools
# crafting materials

materialinventory = {
    "potion_of_hp" : 0,
    "stick": 0,
    "slimeball": 0,
    "slimestring": 0,
    "wood": 0,
    "copper_ore": 0,
    "tin_ore": 0,
    "coal": 0,
    "iron_ore": 0,
    "uranium": 0,
    "cobalt": 0,
    "obsidian": 0,
    "sunken_element": 0,
    "dragon_scale": 0,
    "mythalis": 0,
    "withersteel": 0,
    "graphite": 0,
    "graphene": 0,
    "tridium": 0,
    "shellite": 0,
    "tektite": 0,
    "seraphine": 0,
    "shadowis": 0,
    "aequalis": 0,

    "grue_tooth": 0,
    "copper": 0,
    "bronze": 0,
    "iron": 0,
    "steel": 0,
    "bluesteel": 0,
    "obsidiansteel": 0,
    "sunkensteel": 0

}

grasslandsloot = ["stick","stick","stick","stick","chest"] # locational loot
caveloot = ["copper_ore","copper_ore","coal","coal","chest","tin_ore","tin_ore"]
deepcaveloot = ["iron_ore","iron_ore","coal","coal","coal","uranium"]
imperialoutpostloot = ["cobalt","cobalt","cobalt","steel","steel","steel"]
desertloot = ["copper_ore","copper_ore","iron_ore"]
banditoutpostloot = ["steel","steel","bluesteel","bluesteel","chest"]
lakeloot = ["sunken_element","sunken_element","sunken_element","coal"]
loot = [
    "copper_sword", 
    "copper_sword", 
    "copper_sword",
    "bronze_sword",
    "bronze_sword", 
    "iron_sword", 
    "iron_sword", 
    "potion_of_hp", 
    "leather_armor", 
    "leather_armor", 
    "steel_sword"
    ] # chest loot
# enemies loot
slimeloot = ["slimeball","slimestring"]
banditloot = ["copper_sword","copper_sword","potion_of_hp","copper_sword","copper_sword","potion_of_hp","leather_armor","banditmap","banditmap","banditmap"]
warlockloot = ["leather_armor","potion_of_hp"]
grueloot = ["grue_tooth"]
hollowedloot = ["obsidian","steel","steel","steel","obsidian"]
knightloot = ["steel","steel","steel","bluesteel_sword","knight_armor"]
bandit_officerloot = ["iron_sword","iron_sword","copper_armor","potion_of_hp"]
marauderloot = ["iron_sword"]
bandit_captainloot = ["steel_sword","steel_armor"]

# inventory
inventory = []
# weapon and armor check (so you dont equip like a stick to your inventory)
weapons = [
            "wooden_sword","bronze_sword","copper_sword","iron_sword","steel_sword", "obsidiansteel_sword","bluesteel_sword","grue_tooth_spear", "sunkensteel_armor"
            ]
armors = [
        "leather_armor","copper_armor", "bronze_armor", "iron_armor", "steel_armor", "obsidiansteel_armor", "knight_armor","bluesteel_armor", "sunkensteel_armor"
         ]

grasslandsenemies = ["slime", "slime", "slime", "slime", "slime", "bandit", "bandit", 'warlock', "grue"]
caveenemies = ["grue"]
deepcaveenemies = ["hollowed","grue","grue"]
imperialoutpostenemies = ["knight"]
desertenemies = ["bandit","bandit","bandit","bandit_officer"]
banditoutpostenemies = ["marauder","marauder","marauder","marauder","marauder","bandit_officer","bandit_officer","bandit_officer","bandit_officer","bandit_captain"]
lakeenemies = ["slime"]
deepseaenemies = ["sunken_warrior","sunken_warrior","sunken_warrior","sunken_warrior","sunken_warrior","leviathan","leviathan","Shelia, Queen of the Sea"]
enemychance = 5 # 20%

location = 1 # location of the player


hp = 5 # this should be the hp_cap
hp_cap = 5 # the health cap of the player, this can be increased by armor.
weaponstats = [4,1] # damage and attack speed, calculated by DMG * ATK
playerstats = [1,1] # base damage, base attack speed, added before. These can be affected by armor weight, or armor curses.


# DO NOT CHANGE THESE STARTING STATS!! THESE ARE FIXED!!
action = "none"
enemycorpse = False
enemycorpsetype = "none"
enemyhp = 0
enemyattack = 0
opponent = "none"
weapon = "wooden_sword"
armor = "rags"
runs = 5
enemyheal = 0
enemyhealchance = 0
defense = 0
# intro
print("text based rpg game")
print(" by trr2284 ") # replace with your name if you are modding
print("version 0.1.4 ALPHA, EXPECT BUGS")

# one time stats
onetimestats = {
    "banditmap": False
}


# update weapon and armor stats (IMPORTANT!!)
def statupdateweapon():
    global weapon
    global weaponstats
    global armor
    global weaponstats
    global hp_cap
    global hp
    if weapon == "wooden_sword":
        weaponstats = [4,1]
    
    elif weapon == "copper_sword":
        weaponstats = [6,1]
    
    elif weapon == "bronze_sword":
        weaponstats = [8,0.75]
    
    elif weapon == "iron_sword":
        weaponstats = [10,0.75]
    elif weapon == "steel_sword":
        weaponstats = [12,0.75]
    elif weapon == "grue_tooth_spear":
        weaponstats = [12,0.9]
    elif weapon == "bluesteel_sword":
        weaponstats = [15,0.8]
    elif weapon == "obsidiansteel_sword":
        weaponstats = [20,0.8]
    elif weapon == "sunkensteel_sword":
        weaponstats = [300,0.1]
    textgame()
    

def statupdatearmor():
    global weapon
    global weaponstats
    global armor
    global weaponstats
    global hp_cap
    global hp
    global defense
    
    if armor == "rags":
        hp_cap = 5
    elif armor == "leather_armor":
        hp_cap = 7
    elif armor == "copper_armor":
        hp_cap = 10
    elif armor == "bronze_armor":
        hp_cap = 12
    elif armor == "iron_armor":
        hp_cap = 15
    elif armor == "steel_armor":
        hp_cap = 20
    elif armor == "bluesteel_armor":
        hp_cap = 25
    elif armor == "knight_armor":
        hp_cap = 30
        playerstats == [1, 0.5]
    elif armor == "obsidiansteel_armor":
        hp_cap = 35
    elif armor == "sunkensteel_armor":
        hp_cap = 50
        defense = 5
        playerstats == [0.5,0.25]
    else:
        print("ERROR: stats could not be found, game forcefully terminated! \n Screenshot and send entire terminal to trr2284")
    textgame()





# initate combat with the player
def combatinit():
    global enemyattack
    global enemyhp
    global opponent
    global enemyheal
    global enemyhealchance

    if location == 1:
        opponent = random.choice(grasslandsenemies)
    elif location == 2:
        opponent = random.choice(caveenemies)
    elif location == 3:
        opponent = random.choice(deepcaveenemies)
    elif location == 4:
        opponent = random.choice(imperialoutpostenemies)
    elif location == 5:
        opponent = random.choice(desertenemies)
    elif location == 6:
        opponent = random.choice(banditoutpostenemies)
    elif location == 8:
        opponent = random.choice(deepseaenemies)

    
    if opponent == "slime":
        enemyhp = 2
        enemyattack = 1
    elif opponent == "bandit":
        enemyhp = 5
        enemyattack = 2
    elif opponent == "warlock":
        enemyhp = 5
        enemyattack = 3
    elif opponent == "grue":
        enemyattack = 5
        enemyhp = 7
    elif opponent == "hollowed":
        enemyattack = 5
        enemyhp = 15
    elif opponent == "knight":
        enemyattack = 4
        enemyhp = 12
    elif opponent == "bandit_officer":
        enemyhp = 10
        enemyattack = 4
    elif opponent == "marauder":
        enemyhp = 8
        enemyattack = 3
    elif opponent == "bandit_captain":
        enemyhp = 15
        enemyattack = 5
    elif opponent == "sunken_warrior":
        enemyhp = 20
        enemyattack = 7
    elif opponent == "leviathan":
        enemyhp = 30
        enemyattack = 10
    elif opponent == "Shelia, Queen of the Sea":
        enemyhp = 50
        enemyattack = 7
        enemyhealchance = 5
        enemyheal = 5
    print("you are going against a", opponent)
    combat()

# combat system
def combat():
    global enemyattack
    global enemyhp
    global opponent
    global enemycorpse
    global hp
    global hp_cap
    global enemycorpsetype
    global materialinventory
    global runs
    global enemyhealchance
    global enemyheal
    global defense

    combat_action = "none"

    combat_action = input("i want to fight/use/run     ")

    if combat_action == "fight" or combat_action == "f":
        enemyhp = enemyhp - weaponstats[0] * weaponstats[1] + (playerstats[0] * playerstats[1])
        if enemyhp <= 0:
            print("the enemy died")
            enemycorpsetype = opponent
            enemycorpse = True
            runs += 1
            if runs > 5:
                runs = 5
            textgame()
        else:
            print("you dealt", weaponstats[0] * weaponstats[1] + (playerstats[0] * playerstats[1]), "damage to", opponent )
        print("enemy dealt", enemyattack, "damage, you have", hp - enemyattack, "remaining")
        if enemyhealchance > 0:
            healcheck = random.randrange(1,enemyhealchance)
            if healcheck == 1:
                enemyhp += enemyheal
                print("enemy healed by", enemyheal , "hp")
            else:
                print("enemy dealt", enemyattack, "damage, you have", hp - enemyattack, "remaining")
                hp -= enemyattack - defense
        else:
            print("enemy dealt", enemyattack, "damage, you have", hp - enemyattack, "remaining")
            hp -= enemyattack - defense
        if hp <= 0:
            print("you died!! x_x")
            exit()
        combat()
    
    
    elif combat_action == "use" or combat_action == "u":
        if enemyhealchance > 0:
            healcheck = random.randrange(1,enemyhealchance)
            if healcheck == 1:
                enemyhp += enemyheal
            else:
                print("enemy dealt", enemyattack, "damage, you have", hp - enemyattack, "remaining")
                hp -= enemyattack
        else:
            print("enemy dealt", enemyattack, "damage, you have", hp - enemyattack, "remaining")
            hp -= enemyattack - defense
        if hp <= 0:
            print("you died!! x_x")
            exit()
        if materialinventory["potion_of_hp"] > 0:
            materialinventory["potion_of_hp"] -= 1
            print("potion used sucessfully")
            hp += math.floor((hp_cap / 100) * 60)
            if hp > hp_cap:
                hp = hp_cap
            textgame()
        else:
            print("you dont have an hp potion to use!")
            combat()
    
    
    elif combat_action == "run" or combat_action == "r":
        if runs > 0:
            print("you ran, coward.")
            runs -= 1
            textgame()
        else:
            print("youre tired from running, you must fight")
            textgame()
    elif combat_action == "debug":
        eval(input())
        combat()
    else: 
        print("invalid command")
    combat()




# the actual game
def textgame():
    global action
    global armor
    global enemycorpse
    global weapon
    global hp_cap
    global hp
    global materialinventory
    global location
    global weapons
    global armors
    global enemychance


    action = input("type in player input here, type 'help' for a list of commands   ")
    if action == "help":
        print(" explore: lets you explore \n harvest: lets you harvest the corpse of any enemies \n end: ends the game \n use: use an item or discard it \n equip: equips an item to your stat slot \n dispose: lets you discard unwanted items \n craft: lets you craft gear and materials \n travel: lets you travel to various locations. \n check lets you check all your stats")
        textgame()
    
    
    
    
    
    elif action == "explore" or action == "1":
        i = random.randrange(1, enemychance)
        if i == 1:
            print("in danger, your life is at risk!")
            combatinit()
        else:
            x = random.randrange(1,3)
            if x != 1:
                print("you found nothing, but there were no enemies either.")
                textgame()
            else:
                if location == 1:
                    foundloot = random.choice(grasslandsloot)
                elif location == 2:
                    foundloot = random.choice(caveloot)
                elif location == 3:
                    foundloot = random.choice(deepcaveloot)
                elif location == 4:
                    foundloot = random.choice(imperialoutpostloot)
                elif location == 5:
                    foundloot = random.choice(desertloot)
                elif location == 6:
                    foundloot = random.choice(banditoutpostloot)
                elif location == 7:
                    foundloot = random.choice(lakeloot)
                elif location == 8:
                    foundloot = "nil"
                    print("you cant find anything here other than fish")
                    textgame()
                else:
                    print("an error occured with exploring, the proper place id was not retrieved")
                if foundloot == "chest":
                    foundloot = random.choice(loot)
                    print("you found a", foundloot, "from a chest" )
                    inventory.append(foundloot)
                    textgame()
                else:
                    print("you found a", foundloot )
                    if foundloot == "potion_of_hp":
                        materialinventory["potion_of_hp"] += 1
                        textgame()
                    elif foundloot == "stick":
                        materialinventory["stick"] += 1
                        textgame()
                    elif foundloot == "copper_ore":
                        materialinventory["copper_ore"] += 1
                        textgame()
                    elif foundloot == "coal":
                        materialinventory["coal"] += 1
                        textgame()
                    elif foundloot == "tin_ore":
                        materialinventory["tin_ore"] += 1
                        textgame()
                    elif foundloot == "iron_ore":
                        materialinventory["iron_ore"] += 1
                        textgame()
                    elif foundloot == "uranium":
                        materialinventory["uranium"] += 1
                        textgame()
                    elif foundloot == "cobalt":
                        materialinventory["cobalt"] += 1
                        textgame()
                    elif foundloot == "bluesteel":
                        materialinventory["bluesteel"] += 1
                        textgame()
                    elif foundloot == "sunken_element":
                        materialinventory["sunken_element"] += 1
                        textgame()
                    else:
                        inventory.append(foundloot)
                        textgame()
    
    
    
    elif action == "use" or action == "2":
        if materialinventory["potion_of_hp"] > 0:
            materialinventory["potion_of_hp"] -= 1
            print("potion used sucessfully")
            hp += math.floor((hp_cap / 100) * 60)
            if hp > hp_cap:
                hp = hp_cap
            textgame()
        else:
            print("you dont have an hp potion to use!")
            textgame()
    
    
    
    
    
    
    elif action == "harvest" or action == "3":
        if enemycorpse == True:
            
            
            if enemycorpsetype == "slime":
                foundloot = random.choice(slimeloot)
                print("you found a", foundloot)
                enemycorpse = False
                if foundloot == "slimeball":
                    materialinventory["slimeball"] += 1
                    enemycorpse = False
                    textgame()
                elif foundloot == "slimestring":
                    materialinventory["slimestring"] += 1
                    enemycorpse = False
                    textgame()
                else:
                    inventory.append(foundloot)
                    enemycorpse = False
                    textgame()



            elif enemycorpsetype == "bandit":
                
                foundloot = random.choice(banditloot)
                print("you found a", foundloot )
                if foundloot == "potion_of_hp":
                    materialinventory["potion_of_hp"] += 1
                    enemycorpse = False
                    textgame()
                elif foundloot == "banditmap":
                    onetimestats["banditmap"] = True
                    print("banditoutpost location unlocked")
                else:
                    inventory.append(foundloot)
                    enemycorpse = False
                    
                    textgame()
                enemycorpse = False


            elif enemycorpsetype == "warlock":
                foundloot = random.choice(warlockloot)
                print("you found a", foundloot )
                if foundloot == "potion_of_hp":
                    materialinventory["potion_of_hp"] += 1
                    enemycorpse = False
                    textgame()
                else:
                    inventory.append(foundloot)
                    enemycorpse = False
                    textgame()
                enemycorpse = False


            elif enemycorpsetype == "grue":
                foundloot = random.choice(grueloot)
                print("you found a", foundloot )
                if foundloot == "grue_tooth":
                    materialinventory["grue_tooth"] += 1
                    enemycorpse = False
                    textgame()
                else:
                    print('an error occured when retrieving from the grue loot pool')
                enemycorpse = False
            
            elif enemycorpsetype == "hollowed":
                foundloot = random.choice(hollowedloot)
                print("you found a", foundloot)
                if foundloot == "obsidian":
                    materialinventory["obsidian"] += 1
                    enemycorpse = False
                    textgame()
                    
                elif foundloot == "steel":
                    materialinventory["steel"] += 1
                    enemycorpse = False
                    textgame()
                textgame()
            
            elif enemycorpsetype == "knight":
                foundloot = random.choice(knightloot)
                print("you found a", foundloot)
                if foundloot == "steel":
                    materialinventory["steel"] += 1
                    enemycorpse = False
                    textgame()
                else:
                    inventory.append(foundloot)
                    textgame()
            elif enemycorpsetype == "bandit_officer":
                foundloot = random.choice(bandit_officerloot)
                print("you found a", foundloot)
                inventory.append(foundloot)
                textgame()
            elif enemycorpsetype == "marauder":
                foundloot = random.choice(marauderloot)
                print("you found a", foundloot)
                inventory.append(foundloot)
                textgame()
            elif enemycorpsetype == "bandit_captain":
                foundloot = random.choice(marauderloot)
                print("you found a", foundloot)
                inventory.append(foundloot)
                textgame()
            elif enemycorpsetype == "sunken_warrior":
                materialinventory["sunken_element"] += 10
                print("found 10 sunken elements")
                textgame()
            elif enemycorpsetype == "leviathan":
                materialinventory["sunken_element"] += 25
                print("found 25 sunken elements")
                textgame()
            elif enemycorpsetype == "Shelia, Queen of the Sea":
                materialinventory["sunken_element"] += 250
                print("found 250 sunken elements")
                textgame()
            else:
                print("ERROR: a bug occured when trying to retrieve from loot pools. Game forcefully terminated!")
                exit()
            enemycorpse = False
            
        else:
            print("theres nothing there to harvest...")
        textgame()
    
    
    
    elif action == "end":
        print("exiting game...")
        exit()
    
    
    
    
    
    
    
    elif action == "equip" or action == "4":
        print("what would you like to equip your inventory has", inventory, "weapon/armor")
        
        equip = input()
        
        if equip == "weapon":
            previousequip = weapon
            weaponequip = input("what would you like to equip    ")
            if weaponequip in inventory and weaponequip in weapons:
                #continue
                inventory.append(previousequip)
                inventory.pop(inventory.index(weaponequip))
                print(weaponequip, "has been equipped")
                weapon = weaponequip
                statupdateweapon()
                
                    
            else:
                print("There is no such weapon!")
                textgame()
                
        if equip == "armor":
            previousequip = armor
            armorequip = input("what would you like to equip    ")
            if armorequip in inventory and armorequip in armors:
                #continue
                inventory.append(previousequip)
                inventory.pop(inventory.index(armorequip))
                print(armorequip, "has been equipped")
                armor = armorequip
                statupdatearmor()    
            else:
                print("There is no such armor!")
                textgame()
                
        
        else:
            textgame()


    
    elif action == "dispose" or action == "5":
        print("what would you like to dispose, you have", inventory)
        dispose = input()
        if dispose in inventory:
            inventory.pop(inventory.index(dispose))
            print("disposed")
            textgame()
        else:
            print("you disposed nothing")
        textgame()

    elif action == "travel":
        travelrequest = input("where would you like to travel   ")
        if travelrequest == "caves":
            print("travelled to caves")
            location = 2
            enemychance = 10
            textgame()
        elif travelrequest == "grasslands":
            print('travelled to grasslands')
            location = 1
            enemychance = 5
            textgame()
        elif travelrequest == "deepcaves":
            if location == 2:
                print("travelled to the deeper caves")
                location = 3
                enemychance = 5
                textgame()
        elif travelrequest == "imperial_outpost":
            if location != 2 or location != 3:
                print("travelled to the imperial outpost")
                location = 4
                enemychance = 2
                textgame()
            else:
                print("you are too far away to travel to the imperial outpost")
                textgame()
        elif travelrequest == "desert":
            if location != 2 or location != 3:
                print("travelled to the desert")
                location = 5
                enemychance = 5
            else:
                print("you are too far away to travel to the desert")
        elif travelrequest == "banditoutpost" and onetimestats["banditmap"] == True:
            if location == 5:
                print("travelled to bandit outpost")
                location = 6
                enemychance = 3
                textgame()
            elif onetimestats["banditmap"] == False:
                print("you have no idea where that is")
                textgame()
            else:
                print("you are too far away to travel there")
                textgame()
        elif travelrequest == "lake":
            if location != 2 or location != 3 or location != 5 or location != 6:
                print("travelled to lake")
                location = 7
                enemychance = 100
                textgame()
            else:
                print("you are too far away to travel to the lake")
                textgame()
        elif travelrequest == "deepsea":
            if location == 7:
                print("travelled to the deep sea \n A SENSE OF THALASSOPHOBIA WASHES OVER YOU...")
                location = 8
                enemychance = 5
                textgame()
            else:
                print("you are too far away to enter the sea")
                textgame()
        else:
            print("invalid location")
            textgame()
    
    elif action == "craft" or action == "6":
        craftingrequest = input("what would you like to craft / type help for recipes   ")
        if craftingrequest == "copper":
            if materialinventory["copper_ore"] > 0 and materialinventory["coal"] > 0:
                materialinventory["copper_ore"] -= 1
                materialinventory["coal"] -= 1
                materialinventory["copper"] += 1
                print("copper ingot smelted")
                textgame()
            else:
                print("you dont have enough resources for copper \n copper recipe: 1x copper ore, 1x coal")
        elif craftingrequest == "copper_armor":
            if materialinventory["copper"] > 4:
                materialinventory["copper"] -= 5
                inventory.append("copper_armor")
                print("copper armor forged successfully")
                textgame()
            else:
                print("you dont have enough resources for copper armor \n copper armor recipe: 5x copper")
                textgame()
        elif craftingrequest == "copper_sword":
            if materialinventory["copper"] > 1 and materialinventory["stick"] > 0:
                materialinventory["copper"] -= 2
                materialinventory["stick"] -= 1
                inventory.append("copper_sword")
                print("copper sword forged successfully")
                textgame()
        elif craftingrequest == "grue_tooth_spear":
            if materialinventory["grue_tooth"] > 0 and materialinventory["stick"] > 0:
                materialinventory["grue_tooth"] -= 1
                materialinventory["stick"] -= 1
                inventory.append("grue_tooth_spear")
                print("grue tooth spear crafted sucessfully")
                textgame()
            else:
                print("you dont have enough resources for grue tooth spear \n grue tooth spear recipe: 1x grue tooth, 1x stick")
                textgame()
        elif craftingrequest == "bronze":
            if materialinventory["copper_ore"] > 0 and materialinventory["tin_ore"] > 0 and materialinventory["coal"] > 1:
                materialinventory["copper_ore"] -= 1
                materialinventory["tin_ore"] -= 1
                materialinventory["coal"] -= 2
                materialinventory["bronze"] += 1
                print("bronze sucessfully alloyed")
                textgame()
            else:
                print("you dont have enough resources for bronze \n bronze recipe: 1x copper ore, 1x tin ore, 1x coal")
                textgame()
        elif craftingrequest == "bronze_sword":
            if materialinventory["bronze"] > 1 and materialinventory["stick"] > 0:
                materialinventory["bronze"] -= 2
                materialinventory["stick"] -= 1
                inventory.append("bronze_sword")
                print("bronze sword successfully forged")
                textgame()
            else:
                print("you dont have enough resources for bronze \n bronze recipe: 1x copper ore, 1x tin ore, 2x coal")
                textgame()
        elif craftingrequest == "bronze_armor":
            if materialinventory["bronze"] > 4:
                materialinventory["bronze"] -= 5
                inventory.append("bronze_armor")
                print("bronze armor forged")
                textgame()
            else:
                print("you dont have enough resources for bronze armor \n bronze armor recipe: 5x bronze")
                textgame()
        elif craftingrequest == "iron":
            if materialinventory["iron_ore"] > 0 and materialinventory["coal"] > 0:
                materialinventory["iron_ore"] -= 1
                materialinventory["coal"] -= 1
                materialinventory["iron"] += 1
                print("iron ingot smelted")
                textgame()
            else:
                print("you dont have enough resources for iron \n iron recipe: 1x iron, 1x coal")
                textgame()
        
        elif craftingrequest == "iron_sword":
            if materialinventory["iron"] > 1 and materialinventory["stick"] > 0:
                materialinventory["iron"] -= 2
                materialinventory["stick"] -= 1
                inventory.append("iron_sword")
                print("iron sword forged")
                textgame()
            else:
                print("you dont have neough resources for iron sword \n iron sword recipe: 2x iron, 1x stick")
                textgame()
        elif craftingrequest == "iron_armor":
            if materialinventory["iron"] > 4:
                materialinventory["iron"] -= 5
                inventory.append("iron_armor")
                print("iron armor forged")
                textgame()
            else:
                print("you dont have enough resources for iron armor \n iron armor recipe: 5x iron")
                textgame()
            
            if materialinventory == "steel":
                if materialinventory["iron"] > 1 and materialinventory["coal"] > 0:
                    materialinventory["iron"] -= 2
                    materialinventory["coal"] -= 1
                    materialinventory["steel"] += 1
                    print("steel alloyed")
                    textgame()
                else:
                    print("you dont have enough resources for steel \n steel recipe: 2x iron, 1x coal")
                    textgame()
            
        elif craftingrequest == "steel_sword":
            if materialinventory["steel"] > 1 and materialinventory["stick"] > 0:
                materialinventory["steel"] -= 2
                materialinventory["stick"] -= 1
                inventory.append("steel_sword")
                print("steel sword forged")
                textgame()
            else:
                print("you dont have enough resources for steel sword \n steel sword recipe: 2x steel, 1x stick")
                textgame()
        elif craftingrequest == "steel_armor":
            if materialinventory["steel"] > 4:
                materialinventory["steel"] -= 5
                inventory.append("steel_armor")
                print("steel armor forged")
                textgame()
            else:
                print("you dont have enough resources for steel armor \n steel armor recipe: 5x steel")
                textgame()
        elif craftingrequest == "obsidiansteel":
            if materialinventory["steel"] > 0 and materialinventory["obsidian"] > 1:
                materialinventory["obsidian"] -= 1
                materialinventory["steel"] -= 1
                materialinventory["obsidiansteel"] += 1
                print("obsidiansteel alloyed")
                textgame()
            else:
                print("you dont have enough resources for obsidiansteel \n obsidiansteel recipe: 1x steel, 2x obsidian")
                textgame()
        
        elif craftingrequest == "obsidiansteel_sword":
            if materialinventory["obsidiansteel"] > 1 and materialinventory["stick"] > 0:
                materialinventory["obsidiansteel"] -= 2
                materialinventory["stick"] -=1
                inventory.append("obsidiansteel_sword")
                print("obsidiansteel sword forged")
                textgame()
            else:
                print("you dont have enough resources for obsidiansteel sword \n obsidiansteel sword crafting recipe: 2x obsidiansteel, 1x stick")
                textgame()
        elif craftingrequest == "obsidiansteel_armor":
            if materialinventory["obsidiansteel"] > 4:
                materialinventory["obsidiansteel"] -= 5
                inventory.append("obsidiansteel_armor")
                print("obsidiansteel armor forged")
                textgame()
        
            else:
                print("you dont have enough resources for obsidiansteel armor \n obsidiansteel armor recipe: 5x obsidiansteel")
                textgame()

        elif craftingrequest == "bluesteel":
            if materialinventory["cobalt"] > 2 and materialinventory["steel"] > 0:
                materialinventory["cobalt"] -= 3
                materialinventory["steel"] -= 1
                materialinventory["bluesteel"]
                print("bluesteel alloyed")
                textgame()
            else:
                print("you dont have enough resources for bluesteel \n bluesteel recipe: 3x cobalt, 1x iron")
                textgame()
        elif craftingrequest == "bluesteel_sword":
            if materialinventory["bluesteel"] > 1 and materialinventory["stick"] > 0:
                materialinventory["stick"] -= 1
                materialinventory["bluesteel"] -= 2
                inventory.append("bluesteel_sword")
                print("bluesteel sword forged")
                textgame()
            else:
                print("you dont have enough resources for bluesteel sword \n bluesteel sword recipe: 2x bluesteel, 1x stick")
                textgame()
        elif craftingrequest == "bluesteel_armor":
            if materialinventory["bluesteel"] > 4:
                materialinventory["bluesteel"] -= 5
                inventory.append("bluesteel_armor")
                print("bluesteel armor forged")
                textgame()
            else:
                print("you dont have enough resources for bluesteel armor \n bluesteel armor recipe: 5x bluesteel")
        elif craftingrequest == "potion_of_hp":
            if materialinventory["slimeball"] > 1 and materialinventory["slimestring"] > 1:
                materialinventory["slimeball"] -= 2
                materialinventory["slimestring"] -= 2
                materialinventory["potion_of_hp"] += 1
                print("potion of hp brewed")
                textgame()
            else:
                print("you dont have enough resources for potion of hp \n potion of hp recipe: 2x slimeball, 2x slimestring")
                textgame()
        elif craftingrequest == "sunkensteel":
            if materialinventory["sunken_element"] > 99:
                materialinventory["sunken_element"] -= 100
                materialinventory["sunkensteel"] += 1
                print("forged an incredibly heavy piece of sunkensteel")
                textgame()
            else:
                print("you dont have enough resources for sunkensteel \n sunkensteel recipe: 100x sunken element")
                textgame()
        elif craftingrequest == "sunkensteel_sword":
            if materialinventory["sunkensteel"] > 1 and materialinventory["stick"] > 0:
                materialinventory["sunkensteel"] -= 2
                materialinventory["stick"] -= 1
                inventory.append("sunkensteel_sword")
                print("forged an incredibly heavy sword")
                textgame()
            else:
                print("you dont have enough resources for sunkensteel sword \n sunkensteel sword recipe: 2x sunkensteel, 1x stick")
                textgame()
        elif craftingrequest == "sunkensteel_armor":
            if materialinventory["sunkensteel"] > 4:
                materialinventory["sunkensteel"] -= 5
                inventory.append("sunkensteel_armor")
                print("forged an incredibly heavy sword")
                textgame()
            else:
                print("you dont have enough resources for sunkensteel armor \n sunkensteel armor: 5x sunkensteel")
        elif craftingrequest == "help":
            print("to craft, type the refined material name, such as copper/bronze/iron/steel/bluesteel/obsidiansteel etc, to craft weapons use _sword as the ending, to craft armor use _armor as the ending")
            print("crafting swords will cost two of a material and a stick, while armor will cost five of a material.")
            textgame()
        
        
        else:
            print("invalid crafting recipe")
            textgame()

    elif action == "debug5896": # debugging requires a password to activate, this allows you to directly run python code from the terminal into the game via inventory.append() etc
        eval(input())
        textgame()
    elif action == "check" or action == "7":
        print(materialinventory)
        print("hp:  ", hp)
        print("weapon:  ",weapon)
        print("armor:   ",armor)
        textgame()
    # if all commands fail
    else:
        print("invalid command, try typing the exact thing or type 'help' for commands")
        textgame()

textgame()






