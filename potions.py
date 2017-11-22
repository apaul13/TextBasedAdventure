from .items import Item

class Potion(Item):
    """Potions class"""
    def __init__(self, name, description, heal):
        super().__init__(name, description)
        self.heal = heal

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getHeal(self):
        return self.heal