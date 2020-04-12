import random
chance = random.randint(0,2)
class Monster():
    def __init__(self,name,health,damage,hit,loot=None):
        self.name = name
        self.health = health
        self.damage = damage
        self.hit = hit
        self.loot = [] if loot is None else loot
    def attack():
        pass 
    def run():
        pass
    def cast():
        pass
    def __str__(self):
        return(f'{self.name},{self.health},{self.damage},{self.hit},{self.loot}')