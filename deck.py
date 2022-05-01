import random
import time
from card import *

class Deck:
    def __init__(self):
       self.cardNum = None
       self.cards = []
       self.rows = 5
       self.cols = None    

    def setCardNum(self, number):
        self.cardNum = number

    def getCardNum(self):
        return self.cardNum

    def setCards(self, cardsList):
        self.cards = cardsList    

    def getCard(self, row, col):
        return self.cards[row][col]

    def getRows(self):
        return self.rows

    def setColumns(self, columns):
        self.cols = columns

    def getColumns(self):
        return self.cols

    #Displays the proper card structure asked by the user
    def createDeck(self, difficulty):
        if (int(difficulty)==1):
            self.setColumns(5)
        elif (int(difficulty)==2):
            self.setColumns(11)
        else:
            self.setColumns(14)

        self.randomise(self.cols)


    #Creates a random deck with pairs
    def randomise(self, cols):
        self.setColumns(cols)

        self.cards = [[0 for i in range(self.getColumns())] for j in range(self.getRows())]  

        self.cards[0][0] = " "
        for i in range(1, self.getRows()):
            self.cards[i][0] = i
            
        for i in range(1, self.getColumns()):
            self.cards[0][i] = i

        #Creating the actual cards
        rowsAvail = []
        colsAvail = []
        for i in range(1, self.getRows()):
            rowsAvail.append(i)
        for i in range(1, self.getColumns()):
            colsAvail.append(i)

        usedCards = []  
        while True:     

            #Creating the first card of the pair and placing it in the deck
            firstCard = Card()
            firstCard.randomise(cols)
            while (usedCards.count(firstCard.getName()) > 0):
                firstCard.randomise(cols)

            row = random.choice(rowsAvail)
            col = random.choice(colsAvail)
            while (self.cards[row][col] != 0):
                row = random.choice(rowsAvail)
                col = random.choice(colsAvail)

            self.cards[row][col] = firstCard
            firstCard.setRow(row)
            firstCard.setCol(col)
            usedCards.append(firstCard.getName())

            #Creating the second card and placing it in the deck
            secCard = Card()
            secCard.randomise(cols)
            while (usedCards.count(secCard.getName()) > 0 or secCard.compare(firstCard) == False):
                secCard.randomise(cols)

            row = random.choice(rowsAvail)
            col = random.choice(colsAvail)
            while (self.cards[row][col] != 0):
                row = random.choice(rowsAvail)
                col = random.choice(colsAvail)

            self.cards[row][col] = secCard
            secCard.setRow(row)
            secCard.setCol(col)
            usedCards.append(secCard.getName())
            
            if (self.isFull() == True):
                break


    #Prints the fully visible deck at the start of the game
    def print(self):
        print ("Here is the randomised deck. Try to memorize the matching cards.")  
        print()     

        for i in range(self.getRows()):
            for j in range(self.getColumns()):
                #If the element is on the first row/column, then it is a number. Print the number as is
                if (i == 0 or j == 0): 
                    if (j + 1 > 10):  
                        print(self.cards[i][j], end = "  ") 
                    else:
                        print(self.cards[i][j], end = "   ")  
                else:   
                    if(len(self.cards[i][j].getName()) == 2):  
                        print(self.cards[i][j].getName(), end = "  ") 
                    else:
                        print(self.cards[i][j].getName(), end = " ") 
            print()  
        print()    


    #Prints the deck with all its cards hidden right before the first round
    def printHidden(self):
        print ("The deck will become invisible in 6 seconds.")
        print()
        time.sleep(6)  

        for i in range(self.getRows()):
            for j in range(self.getColumns()):
                if (i == 0 or j == 0): 
                    if (j + 1 > 10):  
                        print(self.cards[i][j], end = "  ") 
                    else:
                        print(self.cards[i][j], end = "   ")  
                else: 
                    print(self.cards[i][j].getHiddenName(), end = "   ") 
            print()
        print()


    #Prints the deck with the the opened cards visible, after every card pick
    def showOpenCards(self):
        for i in range(self.getRows()):
            for j in range(self.getColumns()):

                if (i == 0 or j == 0):  
                    if (j + 1 > 10):  
                        print(self.cards[i][j], end = "  ") 
                    else:
                        print(self.cards[i][j], end = "   ")                
                else:
                    if (self.cards[i][j].isOpen()):
                        if(len(self.cards[i][j].getName()) == 2):  
                            print(self.cards[i][j].getName(), end = "  ") 
                        else:
                            print(self.cards[i][j].getName(), end = " ")  
                    else:
                        print(self.cards[i][j].getHiddenName(), end = "   ")
            print()
        print()


    def hasClosedCards(self):
        """
        >>> deck = Deck()
        >>> deck.createDeck(1)
        >>> deck.hasClosedCards()
        True
        >>> for i in range(1, deck.getRows()):
        ...    for j in range(1, deck.getColumns()):   
        ...        deck.cards[i][j].setOpen()
        >>> deck.hasClosedCards()
        False
        """
        for i in range(1, self.getRows()):
            for j in range(1, self.getColumns()):   
                #If there is at least one closed card, break the loop.
                if (self.cards[i][j].isOpen() == False):
                    return True
        return False


    def isFull(self):
        """
        >>> deck = Deck()
        >>> deck.createDeck(1)
        >>> deck.isFull()
        True
        >>> for i in range(1, deck.getRows()):
        ...    for j in range(1, deck.getColumns()):   
        ...        deck.cards[i][j] = 0
        >>> deck.isFull()
        False
        """
        for i in range(1, self.getRows()):
            for j in range(1, self.getColumns()):   
                if (self.cards[i][j] == 0):
                    return False
        return True


if __name__ == "__main__":
    import doctest
    doctest.testmod() 