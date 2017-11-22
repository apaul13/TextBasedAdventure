from .items import Item

class Weapon(Item):
    """Base Class for weapons"""
    def __init__(self, name, damage, description):
        super().__init__(name, description)
        self.damage = damage
    
    def getName(self):
        return self.name

    def getDamage(self):
        return self.damage

    def getDescription(self):
        return self.description
    