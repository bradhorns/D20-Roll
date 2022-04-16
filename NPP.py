import random

#PCs
warlock = {"HP: ": 1000, "DMG: ": 150, "Mag_mod":10}
wizard = {"HP: ": 800, "DMG: ": 100, "Mag_mod":20}
knight = {"HP: ": 1300, "DMG: ": 250, "Mag_mod":5}
#NPCS
troll = {"HP: ": 1500, "DMG: ": 200, "Mag_mod":2}
orc = {"HP: ": 1200, "DMG: ": 260, "Mag_mod":8}
witch = {"HP: ": 800, "DMG: ": 150, "Mag_mod":18}


def hero_physical_attack(damage):
    damage = hero_dmg 
    return damage

def enemy_physical_attack(damage):
    damage = enemy_dmg
    return damage

def hero_magic_attack(roll):
    damage = roll * hero_mag
    return damage

def enemy_magic_attack(roll):
    damage = roll * enemy_mag
    return damage

def hero_def(damage):
    damage *= .5
    return damage

hero = ' '
hero_roll = 0
hero_defend = False
enemy_roll = 0
enemy = ' '

while True:
    print("\n" "-------------D&D light-------------")
    print(                                     )
    print("---- 1) Play ---- 2) Difficulty ---") 
    print(                                     )
    print("-- 3) Character Select - 4) Exit --")
    user_input = input("\n" "What would you like to do? ")
    # enemy = ' '
    # hero = ' '
    # hero_roll = 0
    # enemy_roll = 0
    # damage = 0
    
    
    #Play
    if user_input == "1":

        #Check characters have been selected
        if enemy == ' ' or hero == ' ':
            print("\n" "Please select your characters first")
        elif enemy != ' ' and hero != ' ':
            print(f"You engage in battle with a {enemy}!" "\n")
            hero_hp = hero_hp_full
            enemy_hp = enemy_hp_full
            damage = 0
            while enemy_hp > 0 or hero_hp > 0:
                #User Attacks
                print("-- 1) Physical Attack --")
                print("-- 2) Magic Attack --")
                print("-- 3) Defend --")
                print("-- 4) Run --")
                user_in1 = input("What will you do? : ")
                if user_in1 == "1":
                    hero_roll = random.randrange(1,20)
                    print("\n" f"You rolled {hero_roll}")
                    if hero_roll == 20:
                        print("\n" "Critical Hit!")
                        damage = 2 * hero_physical_attack(damage)
                        enemy_hp -= damage
                        print(f"{enemy} took {int(damage)} physical damage! They have {int(enemy_hp) if enemy_hp > 0 else 0} health remaining!" "\n" )
                    elif hero_roll == 1:
                        print("\n" "Critical Fail!")
                        damage = 0
                        enemy_hp -= damage
                        print(f"{enemy} took {int(damage)} physical damage! They have {int(enemy_hp) if enemy_hp > 0 else 0} health remaining!" "\n" )
                    else:
                        print("\n" "Sucessful Attack!")
                        damage = hero_physical_attack(damage)
                        enemy_hp -= damage
                        print(f"{enemy} took {int(damage)} physical damage! They have {int(enemy_hp) if enemy_hp > 0 else 0} health remaining!" "\n" )
                elif user_in1 == "2":
                    hero_roll = random.randrange(20)
                    print(f"You rolled {hero_roll}")
                    if hero_roll == 20:
                        print("\n" "Critical Hit!")
                        damage = 2 * hero_magic_attack(hero_roll)
                        enemy_hp -= damage
                        print(f"{enemy} took {int(damage)} magical damage! They have {int(enemy_hp) if enemy_hp > 0 else 0} health remaining!" "\n" )
                    elif hero_roll == 1:
                        print("\n" "Critical Fail!")
                        damage = 0
                        enemy_hp -= damage
                        print(f"{enemy} took {int(damage)} magical damage! They have {int(enemy_hp) if enemy_hp > 0 else 0} health remaining!" "\n" )
                    else:
                        print("\n" "Sucessful Attack!")
                        damage = hero_magic_attack(hero_roll)
                        enemy_hp -= damage
                        print(f"{enemy} took {int(damage)} magical damage! They have {int(enemy_hp) if enemy_hp > 0 else 0} health remaining!" "\n" )
                elif user_in1 == "3":
                    print(f"You brace for the {enemy}'s next attack!")
                    hero_defend = True
                elif user_in1 == "4":
                    print("You coward, return when you have more courage!")
                    break
                damage
                

                #Enemy attacks
                enemy_attack_type = random.randrange(1,3)
                
                if enemy_attack_type == 1:
                    enemy_roll = random.randrange(1,21)
                    print(f"{enemy} rolled {enemy_roll}")
                    if enemy_roll == 20:
                        print("\n" "Critical Hit!")
                        damage = 2 * enemy_physical_attack(damage)
                        if hero_defend == True:
                            hero_def(damage)
                        hero_hp -= damage
                        print(f"{hero} took {int(damage)} physical damage! They have {int(hero_hp) if hero_hp > 0 else 0} health remaining!" "\n")
                        hero_defend = False
                    elif enemy_roll == 1:
                        print("\n" "Critical Fail!")
                        damage = 0
                        hero_hp -= damage
                        print(f"{hero} took {int(damage)} physical damage! They have {int(hero_hp) if hero_hp > 0 else 0} health remaining!" "\n")
                    else:
                        print("\n" "Sucessful Attack!")
                        damage = enemy_physical_attack(damage)
                        if hero_defend == True:
                            hero_def(damage)
                        hero_hp -= damage
                        print(f"{hero} took {int(damage)} physical damage! They have {int(hero_hp) if hero_hp > 0 else 0} health remaining!" "\n")
                        hero_defend = False
                
                elif enemy_attack_type == 2:
                    enemy_roll = random.randrange(1,21)
                    print(f"{enemy} rolled {enemy_roll}")
                    if enemy_roll == 20:
                        print("\n" "Critical Hit!")
                        damage = 2 * enemy_magic_attack(enemy_roll)
                        if hero_defend == True:
                            hero_def(damage)
                        hero_hp -= damage
                        print(f"{hero} took {int(damage)} magical damage! They have {int(hero_hp) if hero_hp > 0 else 0} health remaining!" "\n")
                    elif enemy_roll == 1:
                        print("Critical Fail!")
                        damage = 0
                        hero_hp -= damage
                        print(f"{hero} took {int(damage)} magical damage! They have {int(hero_hp) if hero_hp > 0 else 0} health remaining!" "\n")
                    else:
                        print("\n" "Sucessful Attack!")
                        damage = enemy_magic_attack(enemy_roll)
                        if hero_defend == True:
                            hero_def(damage)
                        hero_hp -= damage
                        print(f"{hero} took {int(damage)} magical damage! They have {int(hero_hp) if hero_hp > 0 else 0} health remaining!" "\n") 
            
                if hero_hp <= 0:
                    print("-- GAME OVER YOU LOSE --")
                    hero_hp = hero_hp_full
                    enemy_hp = enemy_hp_full
                    break
                if enemy_hp <= 0:
                    print(f"You've slayed the {enemy}! Congradulations!")
                    hero_hp = hero_hp_full
                    enemy_hp = enemy_hp_full
                    break
   
   
   
   
   
    #Difficulty
    if user_input == "2":
        print("\n" "------------ Difficulty --------------")
        print("\n" "                                      ")
        print("--- 1) Easy ---- 2) Medium ---- 3) Hard ---" "\n")
        diff = input("Select your difficulty: ")
        if diff == "1":
            pass
        elif diff == "2":
            hero_hp_full *= 0.8
            hero_dmg *= 0.8
            hero_mag -= 1
            enemy_hp_full *= 1.2
            enemy_dmg *= 1.2
            enemy_mag += 1
        elif diff == "3":
            hero_hp_full *= 0.6
            hero_dmg *= 0.6
            hero_mag -= 4
            enemy_hp_full *= 1.4
            enemy_dmg *= 1.4
            enemy_mag += 3
        else:
            print("Invalid Selection")
            continue
        #difficulty modifiers
    
    
    #Character Select
    if user_input == "3":
        #character select screen
        print("\n" "--------------------- Heros: -------------------------" "\n")
        print("\n" "Warlock: Health: 1000, Damage: 150, Magic Modifier: 10")
        print("Wizard: Health: 800, Damage: 10, Magic Modifier: 20")
        print("Knight: Health: 1300, Damage: 250, Magic Modifier: 5" "\n") #add more later
        hero = input("Select your Hero: ")
        if hero == "Warlock":
            hero_hp_full = warlock["HP: "]
            hero_dmg = warlock["DMG: "]
            hero_mag = warlock["Mag_mod"]
        elif hero == "Wizard":
            hero_hp_full = wizard["HP: "]
            hero_dmg = wizard["DMG: "]
            hero_mag = wizard["Mag_mod"]
        elif hero == "Knight":
            hero_hp_full = knight["HP: "]
            hero_dmg = knight["DMG: "]
            hero_mag = knight["Mag_mod"]
        print("\n" "-------------------- Villians: ----------------------" "\n")
        print("\n" "Troll: Health: 1500, Damage: 200, Magic Modifier: 2")
        print("Witch: Health: 800, Damage: 10, Magic Modifier: 18")
        print("Orc: Health: 1200, Damage: 260, Magic Modifier: 8" "\n" )
        enemy = input("Select your Villian: ")
        if enemy == "Troll":
            enemy_hp_full = troll["HP: "]
            enemy_dmg = troll["DMG: "]
            enemy_mag = troll["Mag_mod"]
        elif enemy == "Witch":
            enemy_hp_full = witch["HP: "]
            enemy_dmg = witch["DMG: "]
            enemy_mag = witch["Mag_mod"]
        elif enemy == "Orc":
            enemy_hp_full = orc["HP: "]
            enemy_dmg = orc["DMG: "]
            enemy_mag = orc["Mag_mod"]
        #Need to fill stats here
    
    #Exit
    if user_input == "4":
        print("-- Bye, thanks for playing! --")
        break
