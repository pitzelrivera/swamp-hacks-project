class chest:
    def __init__(self, chestName, chestDefinition, inJail, moneyChange):
        self.chestName = chestName
        self.chestDefinition = chestDefinition
        self.inJail = inJail
        self.moneyChange = moneyChange

    def getName(self):
        return self.chestName

    def getDefinition(self):
        return self.chestDefinition

    def getJail(self):
        return self.inJail

    def getMoneyChange(self):
        return self.moneyChange