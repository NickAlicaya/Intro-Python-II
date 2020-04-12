# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    '''docstring for Player'''

    def __init__(self, room, health, attack, inventory=None, weapon_on=None, lvl=1,exp=1):
        self.room = room
        self.health = health
        self.attack = attack
        self.inventory = [] if inventory is None else inventory
        self.weapon_on = None if weapon_on is None else weapon_on
        self.lvl = (exp//1000)+1
        self.exp = exp
    def pick_up(self,item):
        self.inventory.append(item)
        print("You picked-up the item")  #add item to player inventory and remove it from room treasure
    def drop(self,item):
        self.inventory.remove(item)
        print("You dropped the item") #remove item to player inventory and add it to room treasure
    def equip_wpn(self,item):
        self.weapon_on = item
        self.attack = self.attack+item.damage
        e_item = item
        print('You equip:',e_item)    
    def unequip_wpn(self,item):
        self.weapon_on = None
        self.attack = self.attack-item.damage
        print('WPN ON:',self.weapon_on)
        print('Status:',self)    
    def use_potion(self,item):
        self.health = self.health + item.heal
        self.inventory.remove(item)
        print('You used a healing potion.Regained ',item.heal,'health.')
    def __str__(self):
        return ('{self.room},{self.health},{self.attack},{self.inventory}, {self.weapon_on},{self.exp},{self.lvl}'.format(self=self))
   
   
