class player:
    name= ""
    cards = []
    money= 0
    get_out_of_jail_free_cards= 0

    def __init__(self, name, cards):
        self.name = name
        self.cards = []
        self.money = 500
        self.get_out_of_jail_free_cards = 0

    def setMoney(self, input_Money):
        self.money = self.money + input_Money

    def setCards(self, input_Cards):
        self.cards = self.cards.append(input_Cards)

    def setJail(self, numJailFree):
        self.get_out_of_jail_free_cards + numJailFree

    def getName(self):
        return self.name

    def getMoney(self):
        return self.money

    def getJail(self):
        return self.get_out_of_jail_free_cards
    