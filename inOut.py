
#Gets the user's inputs for the game setup and ensures the following:
#The players involved are at least 2,
#The difficulty level is between 1 and 3
def getInputs():
    print("Welcome to the Matching Game!")
    print()
    
    playerNum = input ("Type in the number of people who will be playing: ")
    while (int(playerNum) < 2):
        print ("Not enough players! There should be at least 2 people. Please try again:")
        playerNum = input ("Type in the number of people who will be playing: ")

    difLvl = input ("Type in the difficulty level (1 to 3): ")
    while (int(difLvl) < 1 or int(difLvl) > 3):
        print ("Difficulty level must be between 1 and 3. Please try again:")
        difLvl = input ("Type in the difficulty level (1 to 3): ")

    print()
    return playerNum, difLvl


#Asks the user for a card and gets it ensuring the following:
#The row selected is between 1 and 4,
#The column selected is between 1 and the difficulty level's appropriate column max,
#The card chosen has not been opened already
def readCard(deck):
    row = input ("Row: ")
    while (int(row) < 1 or int(row) > 4):
        print ("Row must be between 1 and 4. Please try again:")
        row = input ("Row: ")

    col = input ("Column: ")
    while (int(col) < 1 or int(col) >= deck.getColumns()):
        print ("Column must be between 1 and", deck.getColumns() - 1, ". Please try again:")
        col = input ("Column: ")

    while (deck.getCard(int(row), int(col)).isOpen()):
        print ("Card in row", row, "and column", col, "has already been opened. Please choose a card that is face down.")
        row = input ("Row: ")
        while (int(row) < 1 or int(row) > 4):
            print ("Row must be between 1 and 4. Please try again:")
            row = input ("Row: ")
        col = input ("Column: ")
        while (int(col) < 1 or int(col) >= deck.getColumns()):
            print ("Column must be between 1 and", deck.getColumns() - 1, ". Please try again:")
            col = input ("Column: ")

    print()
    return row, col
