# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    '''docstring for Player'''

    def __init__(self, room, health, attack, inventory=None):
        self.room = room
        self.health = health
        self.attack = attack
        self.inventory = [] if inventory is None else inventory

    def pick_up(self,item):
        self.inventory.append(item)
        print("You picked-up the item")  #add item to player inventory and remove it from room treasure

    def drop(self,item):
        self.inventory.remove(item)
        print("You dropped the item") #remove item to player inventory and add it to room treasure
    def use():
        pass    

    def __str__(self):
        return ('{self.room},{self.health},{self.attack},{self.inventory}'.format(self=self))
   
   
