from item import Item

class Potion(Item):
    """Potions class"""
    def __init__(self, name, description, heal):
        self.heal = heal
        super().__init__(name, description) 

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getHeal(self):
        return self.heal

class TeenyWeenyHealingPotion(Potion):
    def __init__(self):
        super().__init__(name = "Teeny Weeny Healing Potion", 
                         description = "A teeny weeny little tiny potion that does practically no healing.",
                         heal = 5)

class TeenyHealingPotion(Potion):
    def __init__(self):
        super().__init__(name = "Teeny Healing Potion",
                         description = "A teeny little potion that does a little more healign than the almost worthless\nTeeny Weeny Potion",
                         heal = 10)

class RegularHealingPotion(Potion):
    def __init__(self):
        super().__init__(name = "Healing Potion",
                         description = "A normal potion that does some high-quality healing, but not that high-quality.",
                         heal = 20)

class LargeHealing