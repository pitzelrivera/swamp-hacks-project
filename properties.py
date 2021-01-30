class property:
    name = ""
    color = ""
    price = 0
    isOwned = False
    numHouses = 0
    
    def setName(self, name):
        self.name = name

    def setColor(self, color):
        self.color = color

    def setPrice(self, price):
        self.price = price

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

    def getIsOwned(self):
        return self.isOwned

    def getNumHouses(self):
        return self.numHouses