import random



def dice_roll(rolls , dx):           #can roll any number of any dice.  displays eachroll
    total = 0
    for i in range (rolls):
        die = random.randint (1,dx)
        print (die)
        total += die
    return total

roll = dice_roll(4,6)
print (roll)
exit()

def dice_roll_mute(rolls , dx):           #can roll any number of any dice.  hides  each roll
    total = 0
    for i in range (rolls):
        die = random.randint (1,dx)
        print (die)
        total += die
    return total

roll = dice_roll(4,6)
print (roll)
exit()


# def D6(rolls):                                        
#     total = 0
#     for i in range (rolls):
#         die = random.randint (1,6)
#         print (die)
#         total += die
#     return total

def stat_roll():                    ######needs sorter and 
    total = 0
    rolls = []
    for i in range (4):
        die = random.randomint(1-6)
        rolls.append(die)
    print (rolls)
    sort(rolls)
    total = sum(die[0,2])
    print (rolls)
    print (total)
    return total
    
# def D20(rolls):
#     total = 0
#     for i in range (rolls):
#         die = random.randint (1,20)
#         print (die)
#         total += die
#     return total

character_sheet = {
    "name": "Hero",
    "strength" : 0,
    "dexterity" : 0,
    "constitution": 0,
    "intelligence" : 0,
    "wisdom" : 0,
    "charisma" : 0,

    "hit_points": 0,
    "atack_bonus": 0,
    "armour_class": 0,
    "initive_bonus": 0,
    "charm":0,
    "wepon": 0
}

atributes =["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
# def character_genl(atribute):
    
#     strength_roll = input ("roll for strength!")
#     if strength_roll == "fudge":
#         character_sheet["strength"] = 20
#     else: 
#         character_sheet["strength"] = D6(3)
  
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def character_gen(atributes):
    for i in range (len (atributes)):
        atribute_roll = input (f"roll for {atributes[i]}!")
        
        if atribute_roll == "fudge":
            character_sheet[atributes[i]] = 20
        else: 
            character_sheet[atributes[i]] = D6(3)
    return character_sheet

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TEST_Block~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~generate a character ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# character_sheet = character_gen(atributes)
# print (character_sheet)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~