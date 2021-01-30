def main():
    #import classes and functions
    import Player
    import Property
    import Chance
    import random
    
    #variables
    gameround = 1
    cardDraw
    playerName
    playerOne
    playerTwo
    answer
    
    #welcome messages and construction of players
    print("Welcome to Virtual Monopoly!")
    playerName = input("Player 1 enter your name: ")
    playerOne = Player(playerName, 0)
    print("Welcome, " + playerOne.getName())
    playerName = input("Player 2 enter your name: ")
    playerTwo = Player(playerName, 0)
    
    #construction of properties
    propertyList = [
        prop_1("Mediterranean Avenue", 60, "brown", False, 3),
        prop_2("Baltic Avenue", 60, "brown", False, 3),
        prop_3("St. Charles Place", 140, "purple", False, 3),
        prop_4("State Avenue", 140, "purple", False, 3),
        prop_5("Virginia Avenue", 160, "purple", False, 3),
        prop_6("Kentucky Avenue", 220, "red", False, 3),
        prop_7("Indiana Avenue", 220, "red", False, 3),
        prop_8("Illinois Avenue", 240, "red", False, 3),
        prop_9("Pennsylvania Avenue", "green", 320, False, 3),
        prop_10("North Carolina Avenue", "green", 300, False, 3),
        prop_11("Pacific Avenue", "green", 300, False, 3),
    ]
    Property(propertyList)

    #list of chance cards
    chanceList = [
        ch0("Advance to Go", "Collect $200 Dollars", False, 200),
        ch1("Go to Jail", "Go Directly to Jail, Do not collect $200", True, 0),
        ch2("Get out of Jail Free", "", False, 0),
        ch3("Tax", "Pay poor tax of $15", False, -15),
        ch4("Chairman of the board", "Pay the other player $50", False, -50),
        ch5("You have won a crossword competition", "Collect $100", False, 100),
        ch6("Go to Jail", "Go Directly to Jail, Do not collect $200", True, 0),
        ch7("Buy your friend a birthday gift", "Pay them $50", False, -50)
    ]
    Chance(chanceList)
    
    #game begins
    while gameround <= 10:
        if gameround % 2 == 1:
            print(playerOne.get_Name() + "draw a card!")
        else:
            print(playerTwo.get_Name() + "draw a card!")
        if random.randint(0, 50) % 2 == 0:
            #call properties deck
            cardDraw = random.randint(1,11)
            print(playerOne.getName() + ", you landed on " + propertyList[cardDraw].getName())
            if propertyList[cardDraw].getIsOwned == False: #Make sure property is not owned
                answer = print("Do you want to buy this property? ")
                if answer == "yes" or answer == "Yes":
                    if playerOne.getMoney() < propertyList[cardDraw].getPrice(): #Cannot buy if they have less than the amount
                        print("You do not have enough money to buy this property.")
                    else:
                        propertyList[cardDraw].setOwner(playerOne.getName())
                        print("Congratulations on your new property!")
            else if ()

        else:
            #call chance deck

        
        if playerOne.getMoney() <= 0 or playerTwo.getMoney() <= 0:
            over(playerOne.getMoney(), playerTwo.getMoney())        
        gameround++
        
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
