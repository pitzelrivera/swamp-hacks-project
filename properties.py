class property:
    name = ""
    color = ""
    price = 0
    rent = 0
    isOwned = False
    numHouses = 0
    
    def __init__(self, name, color, price, owned, num):
        self.name = name
        self.color = color
        self.price = price
        self.rent = price/4
        self.isOwned = owned
        self.numHouses = num

    def setIsOwned(self, owned):
        self.isOwned = owned

    def setNumHouses(self, num):
        self.numHouses = num

    def getName(self):
       return self.getName

    def getColor(self):
        return self.color

    def getPrice(self):
        return self.price

    def getRent(self):
        return self.rent

    def getIsOwned(self):
        return self.isOwned

    def getNumHouses(self):
        return self.numHouses
