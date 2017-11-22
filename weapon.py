from items import Item

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

"""Melee"""
    
class TurdSword(Weapon):
    def __init__(self):
        super().__init__(name="Turd Sword",
                        description="A hand-crafted sword that deals very little damage. Kinda smells bad, too.",
                        damage=1)
                        
class Stick(Weapon):
    def __init__(self):
        super().__init__(name="Stick",
                        description="A flimsy stick that fell down from a tree one day and instills terror on anything smaller than an ant.",
                        damage=2)

class SeriousStick(Weapon):
    def __init__(self):
        super().__init__(name="Serious Stick",
                        description="A solid stick that knows what it's doing and doesn't hold back when it comes to dealing some serious blows!",
                        damage=5)

class NerphSword(Weapon):
    def __init__(self):
        super().__init__(name="Nerph Sword",
                        description="A foam sword on the outside. On the inside, there lies a brutal plastic stick that'll sting real bad.",
                        damage=8)

class SwordSword(Weapon):
    def __init__(self):
        super().__init__(name="Sword Sword",
                        description="An actually metal sword that seemingly has had some okay blacksmithing put into it. It's about as sharp as it tastes.",
                        damage=14)

class AuthoritySword(Weapon):
    def __init__(self):
        super().__init__(name="Authority Sword",
                        description="This sword is a sword that ensures its swordliness by behaving like a sword.",
                        damage=18)