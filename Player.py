class Player:
    name = ""
    cards = list(0)
    money = 0
    get_out_of_jail_free_cards = 0

    def __init__(self, name, cards):
        self.name = name
        self.cards = list()
        self.money = 500
        self.get_out_of_jail_free_cards = 0

    def setMoney(self, input_Money):
        self.__money + input_Money

    def setCards(self, input_Cards):
        self.__cards = self.cards.append(input_Cards)

    def setJail(self, numJailFree):
        self.get_out_of_jail_free_cards + numJailFree

    def getName(self):
        return self.name

    def getMoney(self):
        return self.money

    def getJail(self):
        return self.get_out_of_jail_free_cards
