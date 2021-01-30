def main():
    #import classes and functions
    import Player
    import Properties
    import random
    
    #variables
    gameround = 1;
    
    #welcome messages and construction of players
    print("Welcome to Virtual Monopoly!")
    player1Name = input("Player 1 enter your name: ")
    playerOne = Player(player1Name, 0)
    player2Name = input("PLayer 2 enter your name: ")
    playerTwo = Player(player2Name, 0)
    player2Name = input("Player 2 enter your name: ")
    
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
    
    #game begins
    while gameround <= 10:
        if gameround % 2 == 1:
            print(playerOne.get_Name() + "draw a card!")
        else:
            print(playerTwo.get_Name() + "draw a card!")
        if random.randint(0, 50) % 2 == 0:
            #call properties deck
        else:
            #call chance deck
                
        gameround++
        
    #outside of loop. who has most money this person wins
        
if __name__ == "__main__":
    main()