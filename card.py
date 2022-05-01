import random

suitList = ["♣", "♦", "♥", "♠"]
symbolsList1 = ["10", "J", "Q", "K"]
symbolsList2 = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
symbolsList3 = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

class Card:

    def __init__(self):
       self.suit = None   #clubs, diamonds, hearts or shades
       self.symbol = None  #1 to 10 or A, J, Q, K
       self.nameStr = None  #ex. A♣
       self.hiddenName = "X" #to display when the card is faced down
       self.open = False
       self.points = 0
       self.row = 0
       self.col = 0

    def setSymbol(self, newSymbol):
        self.symbol = newSymbol

    def getSymbol(self):
        return self.symbol

    def setName(self):
        self.nameStr = self.symbol + self.suit    

    def getName(self):
        return self.nameStr

    def getHiddenName(self):
        return self.hiddenName

    def setOpen(self):
        self.open = True

    def setClosed(self):
        self.open = False

    def isOpen(self):
        return self.open

    def getPoints(self):
        return self.points

    def setRow(self, newRow):
        self.row = newRow

    def getRow(self):
        return self.row

    def setCol(self, newCol):
        self.col = newCol

    def getCol(self):
        return self.col

    #Creates a random card according to the game's difficulty level
    def randomise(self, columns):
        if (columns == 5):
            self.suit = random.choice(suitList)
            self.symbol = random.choice(symbolsList1)
        elif (columns == 11):
            self.suit = random.choice(suitList)
            self.symbol = random.choice(symbolsList2)
        else:
            self.suit = random.choice(suitList)
            self.symbol = random.choice(symbolsList3)

        self.setName()
        self.computePoints()   


    def computePoints(self):
        """
        >>> card = Card()
        >>> card.setSymbol("A")
        >>> card.computePoints()
        1
        >>> card.setSymbol(5)
        >>> card.computePoints()
        5
        >>> card.setSymbol("J")
        >>> card.computePoints()
        10
        """
        if (self.getSymbol() == "A"):
            self.points = 1
        elif (self.getSymbol() == "J" or self.getSymbol() == "Q" or self.getSymbol() == "K"):
            self.points = 10
        else:
            self.points = int(self.getSymbol())
        return self.points     


    def compare(self, otherCard):
        """
        >>> card1 = Card()
        >>> card1.setSymbol("J")
        >>> card2 = Card()
        >>> card2.setSymbol("A")
        >>> card1.compare(card2)
        False
        >>> card2.setSymbol("10")
        >>> card1.compare(card2)
        False
        >>> card2.setSymbol("J")
        >>> card1.compare(card2)
        True
        """
        return str(self.getSymbol()) == str(otherCard.getSymbol())  


if __name__ == "__main__":
    import doctest
    doctest.testmod()  