class Item():
    '''docstring for Item'''

    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return('{self.name}, {self.description}').format(self=self)      

class Potion(Item):
    '''docstring for Potion Item subclass'''

    def __init__(self,name,description,heal):
        super().__init__(name,description)
        self.heal = heal

class Weapon(Item):
    '''docstring for Weapon Item subclass'''

    def __init__(self,name,description,damage):
        super().__init__(name,description)
        self.damage = damage
    def __str__(self):
        return('{self.name}, {self.description}, {self.damage}').format(self=self)    



    


    
