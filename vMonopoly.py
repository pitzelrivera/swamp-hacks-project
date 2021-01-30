def main():
    #import classes and functions
    from Player import player
    from Property import properties
    from Chance import chancedeck
    import random
    
    #variables
    gameround = 1
    
    #welcome messages and construction of players
    print("Welcome to Virtual Monopoly!")
    playerName = input("Player 1 enter your name: ")
    playerOne = player(playerName, 0)
    print("Welcome, " + playerOne.getName())
    playerName = input("Player 2 enter your name: ")
    playerTwo = player(playerName, 0)

    def playerTurn(gameturn):
        if gameturn % 2 == 1:
            return playerOne
        else:
            return playerTwo
    
    #construction of properties
    propertyList = []
    propertyList.append(properties("Mediterranean Avenue", 60, "brown", False, 3))
    propertyList.append(properties("Baltic Avenue", 60, "brown", False, 3))
    propertyList.append(properties("St. Charles Place", 140, "purple", False, 3))
    propertyList.append(properties("State Avenue", 140, "purple", False, 3))
    propertyList.append(properties("Virginia Avenue", 160, "purple", False, 3))
    propertyList.append(properties("Kentucky Avenue", 220, "red", False, 3))
    propertyList.append(properties("Indiana Avenue", 220, "red", False, 3))
    propertyList.append(properties("Illinois Avenue", 240, "red", False, 3))
    propertyList.append(properties("Pennsylvania Avenue", 320, "green", False, 3))
    propertyList.append(properties("North Carolina Avenue", 300, "green", False, 3))
    propertyList.append(properties("Pacific Avenue", 300, "green", False, 3))

    #list of chance cards
    chanceList = [
        chancedeck("Advance to Go.", "Collect $200 Dollars.", False, 200),
        chancedeck("Go to Jail.", "Go Directly to Jail, Do not collect $200.", True, 0),
        chancedeck("Get out of Jail Free.", "", False, 0),
        chancedeck("Tax.", "Pay poor tax of $15.", False, -15),
        chancedeck("Chairman of the board.", "Pay the other player $50.", False, -50),
        chancedeck("You have won a crossword competition.", "Collect $100.", False, 100),
        chancedeck("Go to Jail.", "Go Directly to Jail, Do not collect $200.", True, 0),
        chancedeck("Buy your friend a birthday gift.", "Pay them $50.", False, -50)
    ]
    
    #game begins
    while gameround <= 10:
        if gameround % 2 == 1:
            print(playerOne.getName() + " draw a card.")
        else:
            print(playerTwo.getName() + " draw a card.")
        if random.randint(0, 50) % 2 == 0:
            #call properties deck
            cardDraw = random.randint(1,10)
            print(playerTurn(gameround).getName() + ", you landed on " + propertyList[cardDraw].getName())
            if propertyList[cardDraw].getIsOwned == False: #Make sure property is not owned
                answer = print("Do you want to buy this property? ")
                if answer == "yes" or answer == "Yes":
                    if playerOne.getMoney() < propertyList[cardDraw].getPrice(): #Cannot buy if they have less than the amount
                        print("You do not have enough money to buy this property.")
                    else:
                        propertyList[cardDraw].setOwner(playerOne.getName())
                        print("Congratulations on your new property!")
            elif propertyList[cardDraw].getIsOwned() == True and propertyList[cardDraw].getOwner() != playerTurn(gameround).getName():
                playerTurn(gameround).setMoney(-propertyList[cardDraw].getRent)
        else:
            #call chance deck
            print(playerTurn(gameround).getName() + ", you picked a Chance Card!")
            cardDraw = random.randint(1,7)
            print("Your card is: " + chanceList[cardDraw].getName() + " " + chanceList[cardDraw].getDefinition())
            
            playerTurn(gameround).setMoney(chanceList[cardDraw].getMoneyChange())
            
            if chanceList[cardDraw].getJail() == True:
                print("Oh no! You're in jail. Pay $200 to get out of jail.")
                playerTurn(gameround).setMoney(-200)
            elif cardDraw == 4 or cardDraw == 7:
                print("The other player gets $50!")
                if playerTurn(gameround).getName() == playerOne:
                    playerTwo.setMoney(50)
                else:
                    playerOne.setMoney(50)
                

        print(playerOne.getName() + ", you currently have " + str(playerTurn(gameround).getMoney()) + " in your bank")

        if playerOne.getMoney() <= 0 or playerTwo.getMoney() <= 0:
            over(playerOne.getMoney(), playerTwo.getMoney())        
        gameround = gameround + 1
        
    #outside of loop. who has most money this person wins
    over(playerOne.getMoney(), playerTwo.getMoney())
    
    
def over(oneMoney, twoMoney):
    if oneMoney > twoMoney:
        print("Player 1 Wins! with a total of $", oneMoney, "!", sep="")
    if oneMoney < twoMoney:
        print("Player 2 Wins! with a total of $", twoMoney, "!", sep="")
    else:
        print("It was a tie! Both player had $", oneMoney, "!", sep="")

        
if __name__ == "__main__":
    main()