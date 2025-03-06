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
    "obsidan": 0,
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
    "obsidansteel": 0

}

grasslandsloot = ["stick","stick","stick","stick","chest"] # locational loot
caveloot = ["copper_ore","copper_ore","coal","coal","chest","tin_ore","tin_ore"]
deepcaveloot = ["iron_ore","iron_ore","coal","coal","coal","uranium"]
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
banditloot = ["copper_sword","copper_sword","potion_of_hp"]
warlockloot = ["leather_armor","potion_of_hp"]
grueloot = ["grue_tooth"]
hollowedloot = ["obsidan","steel","steel","steel","obsidan"]
# inventory
inventory = []
# weapon and armor check (so you dont equip like a stick to your inventory)
weapons = [
            "wooden_sword","bronze_sword","copper_sword","iron_sword","steel_sword", "obsidansteel_sword"
            ]
armors = [
        "leather_armor","copper_armor", "bronze_armor", "iron_armor", "steel_armor", "obsidansteel_armor"
         ]

grasslandsenemies = ["slime", "slime", "slime", "slime", "slime", "bandit", "bandit", 'warlock', "grue"]
caveenemies = ["grue"]
deepcaveenemies = ["hollowed","grue","grue"]
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
armor = "blank"

# intro
print("text based rpg game")
print(" by trr2284 ") # replace with your name if you are modding
print("version 0.0.1 ALPHA, EXPECT BUGS")



# update weapon and armor stats (IMPORTANT!!)
def statupdate():
    global weapon
    global weaponstats
    global armor
    global weaponstats
    global hp_cap
    global hp
    if weapon == "wooden_sword":
        weaponstats = [4,1]
    
    if weapon == "copper_sword":
        weaponstats = [6,1]
    
    if weapon == "bronze_sword":
        weaponstats = [8,0.75]
    
    if weapon == "iron_sword":
        weaponstats = [10,0.75]
    if weapon == "steel_sword":
        weaponstats = [12,0.75]
    if weapon == "grue_tooth_spear":
        weaponstats = [12,0.9]
    if weapon == "obsidansteel_sword":
        weaponstats = [15,0.8]
    
    if armor == "leather_armor":
        hp_cap = 7
        hp = 7
    if armor == "copper_armor":
        hp_cap = 10
        hp = 10
    if armor == "bronze_armor":
        hp_cap = 12
        hp = 12
    if armor == "iron_armor":
        hp_cap = 15
        hp = 15
    if armor == "steel_armor":
        hp_cap = 20
        hp = 20
    if armor == "obsidansteel_armor":
        hp_cap = 25
        hp = 25
    else:
        print("ERROR: stats could not be found, game forcefully terminated! \n Screenshot and send entire terminal to trr2284")
    textgame()





# initate combat with the player
def combatinit():
    global enemyattack
    global enemyhp
    global opponent

    if location == 1:
        opponent = random.choice(grasslandsenemies)
    elif location == 2:
        opponent = random.choice(caveenemies)
    elif location == 3:
        opponent = random.choice(deepcaveenemies)

    
    if opponent == "slime":
        enemyhp = 2
        enemyattack = 1
    elif opponent == "bandit":
        enemyhp = 5
        enemyattack = 2
    elif opponent == "warlock":
        enemyhp = 3
        enemyattack = 3
    elif opponent == "grue":
        enemyattack = 7
        enemyhp = 10
    elif opponent == "hollowed":
        enemyattack = 5
        enemyhp = 20
    
    print("you are going against a", opponent)
    combat()

# combat system
def combat():
    global enemyattack
    global enemyhp
    global invcheck
    global opponent
    global enemycorpse
    global hp
    global hp_cap
    global enemycorpsetype
    global materialinventory

    invcheck = 0
    combat_action = "none"

    combat_action = input("i want to fight/use/run     ")

    if combat_action == "fight":
        enemyhp = enemyhp - weaponstats[0] * weaponstats[1] + (playerstats[0] * playerstats[1])
        if enemyhp <= 0:
            print("the enemy died")
            enemycorpsetype = opponent
            enemycorpse = True
            textgame()
        else:
            print("you dealt", weaponstats[0] * weaponstats[1] + (playerstats[0] * playerstats[1]), "damage to", opponent )
        print("enemy dealt", enemyattack, "damage, you have", hp - enemyattack, "remaining")
        hp -= enemyattack
        if hp <= 0:
            print("you died!! x_x")
            exit()
        combat()
    
    
    elif combat_action == "use":
        hp -= enemyattack
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
    
    
    elif combat_action == "run":
        if hp <= 0:
            print("you died!! x_x")
            exit()
        print("you ran, coward.")
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
        print(" explore: lets you explore \n harvest: lets you harvest the corpse of any enemies \n end: ends the game \n use: use an item or discard it \n equip: equips an item to your stat slot \n dispose: lets you discard unwanted items \n craft: lets you craft gear and materials \n travel: lets you travel to various locations.")
        textgame()
    
    
    
    
    
    elif action == "explore":
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
                    else:
                        inventory.append(foundloot)
                        textgame()
    
    
    
    elif action == "use":
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
    
    
    
    
    
    
    elif action == "harvest":
        if enemycorpse == True:
            
            
            if enemycorpsetype == "slime":
                foundloot = random.choice(slimeloot)
                print("you found a", foundloot)
                enemycorpse = False
                if foundloot == "silmeball":
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
                if foundloot == "potion of hp":
                    materialinventory["potion_of_hp"] += 1
                    enemycorpse = False
                    textgame()
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
                if foundloot == "obsidan":
                    materialinventory["obsidan"] += 1
                    enemycorpse = False
                    textgame()
                    
                elif foundloot == "steel":
                    materialinventory["steel"] += 1
                    enemycorpse = False
                    textgame()
                textgame()
            else:
                print("ERROR: a bug occured when trying to retrieve from loot pools. Game forcefully terminated!")
            
        else:
            print("theres nothing there to harvest...")
        textgame()
    
    
    
    elif action == "end":
        print("exiting game...")
        exit()
    
    
    
    
    
    
    
    elif action == "equip":
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
                statupdate()
                    
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
                statupdate()    
            else:
                print("There is no such armor!")
                textgame()
        else:
            print("i dont understand that!")
            textgame()


    
    elif action == "dispose":
        print("what would you like to dispose, you have", inventory)
        dispose = input()
        if dispose in inventory:
            inventory.pop(dispose)
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
            else:
                print("you are too far away to travel to the deeper caves")
                textgame()
        else:
            print("invalid location")
            textgame()
    
    elif action == "craft":
        craftingrequest = input("what would you like to craft   ")
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
            
            if materialinventory == "steel":
                if materialinventory["iron"] > 1 and materialinventory["coal"] > 0:
                    materialinventory["iron"] -= 2
                    materialinventory["coal"] -= 1
                    materialinventory["steel"] += 1
                    print("steel alloyed")
                    textgame()
                else:
                    print("you dont have enough resources for steel \n steel recipe: 2x iron, 1x coal")
            
        elif craftingrequest == "steel_sword":
            if materialinventory["steel"] > 1 and materialinventory["stick"] > 0:
                materialinventory["steel"] -= 2
                materialinventory["stick"] -= 1
                inventory.append("steel_sword")
                print("steel sword forged")
                textgame()
            else:
                print("you dont have enough resources for steel sword \n steel sword recipe: 2x steel, 1x stick")
        elif craftingrequest == "steel_armor":
            if materialinventory["steel"] > 4:
                materialinventory["steel"] -= 5
                inventory.append("steel_armor")
                print("steel armor forged")
                textgame()
            else:
                print("you dont have enough resources for steel armor \n steel armor recipe: 5x steel")
                textgame()
        elif craftingrequest == "obsidansteel":
            if materialinventory["steel"] > 0 and materialinventory["obsidan"] > 1:
                materialinventory["obsidan"] -= 1
                materialinventory["steel"] -= 1
                materialinventory["obsidansteel"] += 1
                print("obsidansteel alloyed")
                textgame()
            else:
                print("you dont have enough resources for obsidansteel \n obsidansteel recipe: 1x steel, 2x obsidan")
        
        elif craftingrequest == "obsidansteel_sword":
            if materialinventory["obsidansteel"] > 1 and materialinventory["stick"] > 0:
                materialinventory["obsidansteel"] -= 2
                materialinventory["stick"] -=1
                inventory.append("obsidansteel_sword")
                print("obsidansteel sword forged")
                textgame()
            else:
                print("you dont have enough resources for obsidansteel sword \n obsidansteel sword crafting recipe: 2x obsidansteel, 1x stick")
                textgame()
        elif craftingrequest == "obsidansteel_armor":
            if materialinventory["obsidansteel"] > 4:
                materialinventory["obsidansteel"] -= 5
                inventory.append("obsidansteel_armor")
                print("obsidansteel armor forged")
                textgame()
            else:
                print("you dont have enough resources for obsidansteel armor \n obsidansteel armor recipe: 5x obsidansteel")
        
        
        else:
            print("invalid crafting recipe")
            textgame()

    elif action == "debug5896": # debugging requires a password to activate, this allows you to directly run python code from the terminal into the game via inventory.append() etc
        eval(input())
        textgame()
    # if all commands fail
    else:
        print("invalid command, try typing the exact thing or type 'help' for commands")
        textgame()

textgame()






