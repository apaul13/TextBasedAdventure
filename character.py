class Character():

    def __init__(self, name, hp, winner, weapon):
        self.weapon = weapon
        self.name = name
        self.hp = hp
        self.winner = winner
        
    def isAlive(self):
        return self.hp > 0
    
    def getName():
        return self.name

    def getHp():
        return self.hp

    def setWeapon(self, weapon):
        self.weapon = weapon

    def isWinner():
        return self.winner