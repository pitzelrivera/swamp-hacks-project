class chancedeck:

    def __init__(self, chance_name, chance_definition, is_in_jail, money_change) :
        self.name = chance_name
        self.definition = chance_definition
        self.jail = is_in_jail
        self.money = money_change

    def getName(self):
        return self.name

    def getDefinition(self):
        return self.definition

    def getJail(self):
        return self.jail

    def getMoneyChange(self):
        return self.money
