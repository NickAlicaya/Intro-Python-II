from room import Room
from player import Player
from item import Item,Weapon,Potion
import random


# Declare all items
item ={
    'sword': Weapon("Sword", """Sheathed an ornate scabbard, though covered in dust, some light escapes from it""", 20),
    'knife': Weapon("Knife", "Made of some unknown black metal. It's serrated edges promise cutting pain", 10),
    'potion': Potion("Healing_potion", "Drinking this magic potion restores 10 health", 10,),
    'gold': Item("gold_coins", "A small pouch with 10 gold coins")
}
# for i in item:
#     print('xxxxxxxxxx',item[i])

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

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
room['narrow'].add_item(item['potion'])
room['narrow'].add_item(item['gold'])



# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'], 100, 10)
# player.pick_up(str(item['gold']))
# player.drop(str(item['gold']))
# print('PLLLAAAYER',str(player))
# print(f"Current player: {player.room.name,player.health,player.attack}")
# Write a loop that:
while True:
    #
    # * Prints the current room name
    # print(" f'Current Room: \033[1;32;40m{player.room.name}' \u001b[37m \n")
    print(f"\u001b[32mCurrent Room: {player.room.name}")
# * Prints the current description (the textwrap module might be useful here).
    print(f"{player.room.description}\u001b[0m")
    if player.room.treasure == []:
        print("\u001b[33mSadly you see no valuable items you can pickup from this room.")
    else:
        for t in player.room.treasure:
            print("\u001b[33m You find treasure.",t)    
# * Waits for user input and decides what to do.
    move = input("type \u001b[35m[i]\u001b[0m or \u001b[35m[inventory]\u001b[0m to Check Inventory \u001b[35m[take (item-name)]\u001b[0m to Pick up an item\n\u001b[35m[w]\u001b[0m North \u001b[35m[s]\u001b[0m South \u001b[35m[a]\u001b[0m East \u001b[35m[d]\u001b[0m West \u001b[35m[q]\u001b[0m Quit:\n").lower()

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
        elif action_handler[0] == 'drop' or action_handler[0] == 'remove':
            target_item = action_handler[1]
            found=False
            for junk in player.inventory:
                if junk.name.lower() == target_item.lower():
                    found = True
                    player.drop(junk)
                    player.room.add_item(junk)
            if found == False:
                print("Invalid, item does not exist!")  
            else:
                found = False            
# If the user enters "q", quit the game.
    elif move == 'q':
        break
# If the user enters a cardinal direction, attempt to move to the room there.
    elif move == 'w':
        if player.room.n_to != None:
            player.room = player.room.n_to
        else:
            wall()
    elif move == 's':
        if player.room.s_to != None:
            player.room = player.room.s_to
        else:
            wall()
    elif move == 'd':
        if player.room.e_to != None:
            player.room = player.room.e_to
        else:
            wall()
    elif move == 'a':
        if player.room.w_to != None:
            player.room = player.room.w_to
        else:
            wall()
    elif move == 'i' or 'inventory':
        # print(f"\u001b[33mInventory: {player.inventory}\u001b[0m")
        for z in player.inventory:
            print("\u001b[33m INVENTORY:",z.name)                     
    else:
        print("Invalid movement. Press W for North, S for South, A for West, D for East or Q to Quit game")
