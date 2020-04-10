from room import Room
from player import Player
from item import Item,Weapon,Potion
import random


# Declare all items
item ={
    'sword': Weapon("Vorpal", "An exceptionally sharp, magical sword", 20),
    'knife': Weapon("Knife of biting", "It's edges promise cutting pain", 10),
    'potion': Potion("Healing potion", "Restores 10 health", 10,),
    'gold': Item("gold coins", "A small pouch of 10 gold pieces")
}

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
# print(f"Current player: {player.room.name,player.health,player.attack}")
# Write a loop that:
while True:
    #
    # * Prints the current room name
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print(f"Current Room: {player.room.name}")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
# * Prints the current description (the textwrap module might be useful here).
    print(f"{player.room.description}")
    if player.room.treasure == []:
        print("Sadly you see no valuable items you can pickup from this room.")
    else:
        print(player.room.treasure)    
# * Waits for user input and decides what to do.
    move = input("type [i] or 'inventory' to Check Inventory [t] to Search room\n[w] North [s] South [a] East [d] West [q] Quit:\n").lower()

# Print an error message if the movement isn't allowed.
    def wall():
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n      Can't move there, something blocks your way!\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
# If the user enters "q", quit the game.
    if move == 'q':
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
        print(f"Inventory: {player.inventory}")
    # elif move == 't':
    #     print(f"treasure: {player.room.treasure}")   
    #     print("testing from t") 
             
    else:
        print("Invalid movement. Press W for North, S for South, A for West, D for East or Q to Quit game")
