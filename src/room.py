# Implement a class to hold room information. This should have name and
# description attributes.
import random
chance = random.randint(0,3)


class Room():
    '''docstring for Room'''

    def __init__(self, name, description, treasure=None, enemyList=None):
        self.name = name
        self.description = description
        self.treasure = [] if treasure is None else treasure
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.enemyList = [] if enemyList is None else enemyList
    def add_item(self,item):
        self.treasure.append(item)
    def remove_item(self,item):
        self.treasure.remove(item)   
    def __str__(self):
        return(f'{self.name},{self.description},{self.treasure},{self.enemyList}')    
    def battle():
        pass    
    




