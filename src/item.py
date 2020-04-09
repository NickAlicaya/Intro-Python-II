class Item():
    '''docstring for Item'''

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def pick_up():
        pass    
    def drop():
        pass
    def use():
        pass

class Potion(Item):
    '''docstring for Potion Item subclass'''

    def __init__(self,name,description,heal):
        super().__init__(name,description):
        self.heal = heal

class Weapon(Item):
    '''docstring for Weapon Item subclass'''

    def __init__(self,name,description,dmg):
        super().__init__(name,description):
        self.dmg = dmg

    


    
