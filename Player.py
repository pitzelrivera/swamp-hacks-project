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

    def set_Money(self, input_Money):
        self.__money = input_Money

    def set_Cards(self, input_Cards):
        self.__cards = self.cards.append(input_Cards)

    def set_Jail(self, numJailFree):
        self.get_out_of_jail_free_cards + numJailFree

    def get_Name(self):
        return self.name

    def get_Money(self):
        return self.money

    def get_Jail(self):
        return self.get_out_of_jail_free_cards