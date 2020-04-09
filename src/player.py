# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    '''docstring for Player'''

    def __init__(self, room, health, attack, inventory=None):
        self.room = room
        self.health = health
        self.attack = attack
        self.inventory = []
