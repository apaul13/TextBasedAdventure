from item import Item

class Food(Item):
    """Food class"""
    def __init__(self, name, description, heal):
        self.heal = heal
        super().__init__(name, description) 

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getHeal(self):
        return self.heal

class PotatoChips(Food):
    def __init__(self):
        super().__init__(name = "Potato Chips", 
                         description = "Delicious potato chips that do practically no healing.",
                         heal = 5)

class ChocolateBar(Food):
    def __init__(self):
        super().__init__(name = "Chocolate Bar",
                         description = "A scrumptious, high-quality bar of Swiss chocolate. Rather yummy, but not healthy.",
                         heal = 10)

class Milkshake(Food):
    def __init__(self):
        super().__init__(name = "Milkshake",
                         description = "A strawberry milkshake, but you wish it wasn't strawberry, because strawberry is a gross flavor.",
                         heal = 20)

class Cheeseburger(Food):
    def __init__(self):
        super().__init__(name = "Cheese Burger",
                         description = "Nothing beats a nice, delicious, cheese burger. Hope you're not lactose intolerant.",
                         heal = 20)

class FiletMignon(Food):
    def __init__(self):
        super().__init__(name = "Filet Mignon",
                         description = "A beautiful, high-class, scrumptious, perfect filet mignon. Heals you up to 100hp, pretty sweet.",
                         heal = 100)