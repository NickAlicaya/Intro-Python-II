from room import Room
from player import Player
from item import *
from enemies import *
import random

loot=[
    Weapon("Sword", """Sheathed an ornate scabbard, though covered in dust, some light escapes from it""", 20),
    Weapon("Knife", "Made of some unknown black metal. It's serrated edges promise cutting pain", 10),Potion("Healing_potion", "Drinking this magic potion restores 10 health", 10,),
    Item("gold_coins", "A small pouch with 10 gold coins")
    ]

def loot(): 
    lootChance = random.randint(0,3)
    lootDrop = loot[lootChance]
    return lootDrop

#Create Monsters
monsters = [
    Monster('troll', 80,12,350,1),
    Monster('bat',40,8,200,1),
    Monster('goblin',50,10,250,1),
    Monster('orc', 60,10,350,1),
    Monster('giant spider', 60,12,250,1),
    Monster('wyvern', 160,30,750,1),
    Monster('drow', 100,25,400,1),
    Monster('manticore', 130,26,500,1)
]

def selectEnemy():
    chance = random.randint(0,7)
    enemy = monsters[chance]
    return enemy
def youDied():
    print('\u001b[31mYou have died. Thank you for playing\u001b[0m')
    exit()

selectEnemy()

def battleState():
    enemy = selectEnemy()
    print('\u001b[31mYou encounter a wild', enemy.name,'\u001b[0m')
    while enemy.health > 0:
        choice = input('\u001b[34mActions:\n1.Attack\n2.Use item\n3.Check player status\n4.RUN!\u001b[0m')
        if choice == '1':
            print('You swing your weapon at',enemy.name)
            hitchance = random.randint(0,50)
            if hitchance > 3:
                e_dmg = int((random.randint(1,player.attack))*(1+player.lvl/5))
                enemy.health = enemy.health-e_dmg 
                print('You dealt',e_dmg,'damage to',enemy.name)     
                print('Enemy has:',enemy.health,'life left')   
                if enemy.health > 0:
                    e_hitchance = random.randint(0,10)
                    if e_hitchance > 4:
                        p_dmg=int((random.randint(1,enemy.damage))*(1+enemy.lvl/5))
                        player.health = player.health-p_dmg
                        print("\u001b[31m",enemy.name,'strikes you and deals', p_dmg,"damage\u001b[0m")
                        if player.health < 1:
                            youDied()
                    else:
                        print(enemy.name, 'attacks but you dodged the attack.')  

                else:
                    print('You defeated',enemy.name)
                    player.exp = player.exp+enemy.exp
                    print('You gained',enemy.exp,)
                    player.lvl = player.exp//1000
                    reward()           
            else:    
                print('You missed')
        elif choice == '2':
           for option in player.inventory:
                use = input('Which potion do you want to use?').lower()
                if use == option.name.lower():
                    target_potion = option
                    player.use_potion(target_potion)    
                else:
                    print("\u001b[31mYou searched but couldn't find that item. You lose a turn.\u001b[0m")
                   
        elif choice == '4':
            e_hitchance = random.randint(0,10)
            if e_hitchance > 4:
                player.health = player.health-enemy.damage
                print("\u001b[31m",enemy.name,'strikes you and deals', enemy.damage,"damage but you manage to escape.\u001b[0m")
                break
                if player.health < 1:
                    youDied()
                else:
                    print('You ran and escaped to live another day.')
                    break  
            else: 
                print('You live to fight another day.')   
                break      
        elif choice == '3':
            e_hitchance = random.randint(0,10)
            if player.inventory == None or player.inventory == []:
                print('Health: ',player.health,'Equipped weapon: ',player.weapon_on, 'Your inventory is empty')
                if e_hitchance > 4:
                    player.health = player.health-enemy.damage
                    print("\u001b[31m",enemy.name,'strikes you and deals', enemy.damage,"damage\u001b[0m.")
                    if player.health < 1:
                        youDied()
                    else:
                        print('Stop wasting time and concentrate if you want to survive.')
                else: 
                    print("\u001b[31m",enemy.name,'attempts to strike you while you were idle but missed.',"\u001b[0m")   

            else:
                for x in player.inventory:
                    print('You pause and check your current condition','Health:',player.health,'Equipped weapon: ',player.weapon_on,'Inventory: ',x.name,'You lose a turn.')
                    if e_hitchance > 4:
                        player.health = player.health-(enemy.damage*(1+enemy.lvl/10))
                        print("\u001b[31m",enemy.name,'strikes you and deals', enemy.damage,"\u001b[0m.")
                        if player.health < 1:
                            youDied()
                        else:
                            print('Stop wasting time and concentrate if you want to survive.')
                    else: 
                        print(enemy.name,'attempts to strike you while you were idle but missed.')   
                      
        elif choice == 'q':
            break
        else:
            print('Invalid input, type 1, 2 or 3 to make a choice')


# Declare all items
item ={
    'sword': Weapon("Sword", """Sheathed an ornate scabbard, though covered in dust, some light escapes from it""", 20),
    'knife': Weapon("Knife", "Made of some unknown black metal. It's serrated edges promise cutting pain", 10),
    'potion': Potion("Healing_potion", "Drinking this magic potion restores 40 health", 40,),
    'gold': Item("gold_coins", "A small pouch with 10 gold coins"),
    'potion2': Potion("Healing_potion2", "Drinking this magic potion restores 80 health", 80,),
    'mace': Weapon("Mace+1", """A magical mace """, 20),
    'key': Item("rusty_key", "Looks like this might be useful for something later."),
}

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"), 
    'trap':  Room("Trap room",
                     "You walked into a room of traps. Bolts of arrow hit you. The only way out is to go back to the passage east"),            
                            

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north, east and west."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Add treasure to room
room['foyer'].add_item(item['sword'])
room['foyer'].add_item(item['potion'])
room['narrow'].add_item(item['potion'])
room['narrow'].add_item(item['gold'])

def reward():
    z=random.randint(0,7)
    if z == 0:
        pass
    elif z == 1:
        player.room.add_item(item['potion'])
    elif z == 2:
        player.room.add_item(item['knife'])    
    elif z == 3:
        player.room.add_item(item['gold']) 
    elif z == 4:
        player.room.add_item(item['mace'])  
    elif z == 5:
        player.room.add_item(item['potion2'])  
    elif z == 6:
        player.room.add_item(item['key'])                           

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['foyer'].w_to = room['trap']
room['trap'].e_to = room['foyer']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'], 100, 10)

# battleState()
while player.health > 0:
    if player.room == room['trap']:
        player.health = player.health -20
    encounter = random.randint(0,10)
    # * Prints the current room name
    print(f"\u001b[32mCurrent Room: {player.room.name}")
# * Prints the current description (the textwrap module might be useful here).
    print(f"{player.room.description}\u001b[0m")
    if player.room.treasure == []:
        print("\u001b[33mYou see nothing of in this room.")
    else:
        for t in player.room.treasure:
            print("\u001b[33m You find treasure.",t)    
# * Waits for user input and decides what to do.
    move = input("type \u001b[35m[w]\u001b[0m North \u001b[35m[s]\u001b[0m South \u001b[35m[a]\u001b[0m East \u001b[35m[d]\u001b[0m West \u001b[35m[r]\u001b[0m Rest \u001b[35m[c]\u001b[0m available commands \u001b[35m[q]\u001b[0m Quit:\n").lower()

# Print an error message if the movement isn't allowed.
    def wall():
        print("\u001b[31m========================================================\n      Can't move there, something blocks your way!\n========================================================\u001b[0m")
   
    if len(move.split()) == 2:
        action_handler = move.split()
        if action_handler[0] == 'take' or action_handler[0] == 'get':
            target_item = action_handler[1]
            found=False
            for i in player.room.treasure:
                if i.name.lower() == target_item.lower():
                    found = True
                    player.pick_up(i)
                    player.room.remove_item(i)
            if found == False:
                print("Invalid, item does not exist!")   
            else:
                found = False      

        elif action_handler[0] == 'drink':
            target_item = action_handler[1]
            found=False
            for pot in player.inventory:
                if pot.name.lower() == target_item.lower(): 
                    found = True
                    player.use_potion(pot)
            if found == False:
                print("Invalid, item does not exist!")  
            else:
                found = False

        elif action_handler[0] == 'equip':
            target_item = action_handler[1]
            found=False
            for w in player.inventory:
                if w.name.lower() == target_item.lower(): 
                    found = True
                    player.equip_wpn(w)
            if found == False:
                print("Invalid, item does not exist!")  
            else:
                found = False     

        elif action_handler[0] == 'unequip':
            target_item = action_handler[1]
            found=False
            for w in player.inventory:
                if w.name.lower() == target_item.lower(): 
                    found = True
                    player.unequip_wpn(w)
            if found == False:
                print("Invalid, item does not exist!")  
            else:
                found = False  

        elif action_handler[0] == 'drop' or action_handler[0] == 'remove':
            target_item = action_handler[1]
            found=False
            if player.weapon_on == None or player.weapon_on.name.lower() !=  target_item.lower():
                for junk in player.inventory:
                    if junk.name.lower() == target_item.lower():
                        found = True
                        player.drop(junk)
                        player.room.add_item(junk)
                    if found == False:
                        print("Invalid, item does not exist!")  
                    else:
                        found = False   
            else:
                print('Unequip weapon before dropping')

        elif action_handler[0] == 'drink' or action_handler[0] == 'use':
            target_item = action_handler[1]
            found=False
            for p in player.inventory:
                if p.name.lower() == target_item.lower():
                    found = True
                    player.use_potion(p)
                if found == False:
                    print("Invalid, item does not exist!")  
                else:
                    found = False   
               
                       
# If the user enters "q", quit the game.
    elif move == 'q':
        break
    elif move == 'r' or move == 'rest':
        player.health = 100
        player.health = ((player.health)*(1+(player.lvl//4)))

    elif move == 'c':
        print("Available commands: ","\n\u001b[35m[i]\u001b[0m or \u001b[35m[inventory]\u001b[0m to Check Inventory\n\u001b[35m[take (item-name)]\u001b[0m to Pick up an item\n\u001b[35m[drink (potion-name)]\u001b[0m to drink a potion\n\u001b[35m[status]\u001b[0m to check player status")

# If the user enters a cardinal direction, attempt to move to the room there.
    elif move == 'w':
        if player.room.n_to != None:
            player.room = player.room.n_to
            encounter = random.randint(0,10)
            if encounter > 6:
                print('You encounter a random monster!')
                battleState()
        else:
            wall()
            if encounter > 6:
                print('You encounter a random monster!')
                battleState()
    elif move == 's':
        if player.room.s_to != None:
            player.room = player.room.s_to
            if encounter > 6:
                print('You encounter a random monster!')
                battleState()
        else:
            wall()
            if encounter > 6:
                print('You encounter a random monster!')
                battleState()
    elif move == 'd':
        if player.room.e_to != None:
            player.room = player.room.e_to
            if encounter > 6:
                print('You encounter a random monster!')
                battleState()
        else:
            wall()
            if encounter > 6:
                print('You encounter a random monster!')
                battleState()
    elif move == 'a':
        if player.room.w_to != None:
            player.room = player.room.w_to
            if encounter > 6:
                print('You encounter a random monster!')
                battleState()
        else:
            wall()
            if encounter > 6:
                print('You encounter a random monster!')
                battleState()
    elif move == 'status':
        print("\u001b[33m",'Health: ', player.health,'Equipped weapon:',player.weapon_on,'Level:',player.lvl,'Exp:',player.exp,'\n Inventory:',"\u001b[0m")   
        for s in player.inventory:
            print("\u001b[33m",s,"\u001b[0m")      
    elif move == 'i' or 'inventory':
        if player.inventory != []:
            print("\u001b[33m INVENTORY:")
            for z in player.inventory:
                print("\u001b[33m", z.name)   
        else:
            print("\u001b[33m Your Bag is Empty.")                         
    else:
        print("\u001b[31mInvalid movement. Press W for North, S for South, A for West, D for East or Q to Quit game\u001b[0m")
