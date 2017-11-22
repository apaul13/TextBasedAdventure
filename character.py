__author__ = "Austin Paul"

class Character():

    def __init__(self, name, hp, winner):
        self.name = name
        self.hp = hp
        self.winner = winner
        
    def is_alive(self):
        return self.hp > 0