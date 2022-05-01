from inOut import readCard
from card import *

class Player:
    def __init__(self):
       self.name = None
       self.points = 0
       self.firstCard = None 
       self.secCard = None
       self.thirdCard = None
       self.nextMissesFlag = False   
       self.playAgainFlag = None 

    def setName(self, newName):
        self.name = newName

    def getName(self):
        return self.name

    def getPoints(self):
        return self.points

    def addPoints(self, newPoints):
        self.points = self.points + newPoints 

    def setFirstCard(self, newCard):
        self.firstCard = newCard

    def getFirstCard(self):
        return self.firstCard

    def setSecCard(self, newCard):
        self.secCard = newCard

    def getSecCard(self):
        return self.secCard

    def setThirdCard(self, newCard):
        self.thirdCard = newCard

    def getThirdCard(self):
        return self.thirdCard

    def getNextMissesFlag(self):
        return self.nextMissesFlag

    def getPlayAgainFlag(self):
        return self.playAgainFlag

    #The main method of every player
    def playRound(self, deck):
        self.nextMissesFlag = False
        self.playAgainFlag = False
        self.pickFirstCard(deck)
        self.pickSecondCard(deck)


    #Gets the first valid card from the player and displays the updated deck
    def pickFirstCard(self, deck):
        print("Player", int(self.getName()) + 1, "please pick your first card.")
        row, col = readCard(deck)
        deck.cards[int(row)][int(col)].setOpen()

        self.setFirstCard(deck.cards[int(row)][int(col)])
        deck.showOpenCards()  


    #Gets the second valid card from the player.
    #Displays the updated deck and checks for point updates and special pairings
    def pickSecondCard(self, deck):
        print("Player", int(self.getName()) + 1, "please pick your second card.")
        row, col = readCard(deck)
        deck.cards[int(row)][int(col)].setOpen()
        deck.showOpenCards() 

        self.setSecCard(deck.cards[int(row)][int(col)])
        if (self.getSecCard().compare(self.getFirstCard()) == True):
            points = self.getSecCard().getPoints()
            self.addPoints(points)
            print ("Congratulations! You just won", points, "point(s). You have a total of", self.getPoints(), "point(s).")

            if (self.checkForSecondRound(deck) == True):
                self.playAgainFlag = True
            elif (self.checkNextMissesRound() == True):
                self.nextMissesFlag = True

        elif (self.checkForThirdCard() == True):
            self.pickThirdCard(deck)

        else:
            print("Your cards didn't match.")
            print()
            deck.cards[int(self.getFirstCard().getRow())][int(self.getFirstCard().getCol())].setClosed()
            deck.cards[int(row)][int(col)].setClosed()
            deck.showOpenCards() 


    #Gets the third valid card from the player (when allowed) and displays the updated deck.
    #If the player chose 2 Qs (if) they get 10 points and the K becomes faced down.
    #If they chose 2 Ks (elif) they get 10 points, the Q becomes faced down and the next player misses their turn.
    #If none of the cards match (else), all 3 become faced down again.
    def pickThirdCard(self, deck):
        print("Player", int(self.getName()) + 1, "please pick your third card.")
        row, col = readCard(deck)
        deck.cards[int(row)][int(col)].setOpen()

        self.setThirdCard(deck.cards[int(row)][int(col)])
        if (self.getThirdCard().compare(self.getFirstCard())):
            points = self.getFirstCard().getPoints()
            self.addPoints(points)

            deck.cards[int(self.getSecCard().getRow())][int(self.getSecCard().getCol())].setClosed()
            deck.showOpenCards() 
            print("Your first and third cards matched. Your second card turned faced down again.")
            print ("Congratulations! You just won", points, "points. You have a total of", self.getPoints(), "points.")

            self.checkNextMissesRound()
        elif (self.getThirdCard().compare(self.getSecCard())):
            points = self.getSecCard().getPoints()
            self.addPoints(points)

            deck.cards[int(self.getFirstCard().getRow())][int(self.getFirstCard().getCol())].setClosed()
            deck.showOpenCards() 
            print("Your second and third cards matched. Your first card will turn faced down again.")
            print ("Congratulations! You just won", points, "points. You have a total of", self.getPoints(), "points.")

            self.checkNextMissesRound()
        else:
            deck.showOpenCards() 
            deck.cards[int(self.getFirstCard().getRow())][int(self.getFirstCard().getCol())].setClosed()
            deck.cards[int(self.getSecCard().getRow())][int(self.getSecCard().getCol())].setClosed()
            deck.cards[int(row)][int(col)].setClosed()
            print("None of the 3 cards matched. All of them turned faced down again.")
            print()
            deck.showOpenCards() 


    def checkForSecondRound(self, deck):
        """
        >>> from deck import *
        >>> from card import *
        >>> deck = Deck()
        >>> deck.createDeck(1)
        >>> player = Player()
        >>> card = Card()
        >>> card.setSymbol("J")
        >>> player.setSecCard(card)
        >>> player.checkForSecondRound(deck)
        You picked 2 Js, so you get to play again.
        True
        >>> card.setSymbol("10")
        >>> player.setSecCard(card)
        >>> player.checkForSecondRound(deck)
        False
        >>> card.setSymbol("K")
        >>> player.setSecCard(card)
        >>> player.checkForSecondRound(deck)
        False
        """
        if (self.getSecCard().getSymbol() == "J" and deck.hasClosedCards() == True):
            print("You picked 2 Js, so you get to play again.")
            return True
        else:
            return False


    def checkNextMissesRound(self):
        """
        >>> from card import *
        >>> player = Player()
        >>> card1 = Card()
        >>> card1.setSymbol("K")
        >>> card2 = Card()
        >>> card2.setSymbol("K")
        >>> player.setFirstCard(card1)
        >>> player.setSecCard(card2)
        >>> player.checkNextMissesRound()
        You picked 2 Ks, so the next player loses their round.
        True
        >>> card1.setSymbol("Q")
        >>> card2.setSymbol("K")
        >>> player.setFirstCard(card1)
        >>> player.setSecCard(card2)
        >>> player.checkNextMissesRound()
        False
        >>> card1.setSymbol("K")
        >>> card2.setSymbol(5)
        >>> player.setFirstCard(card1)
        >>> player.setSecCard(card2)
        >>> player.checkNextMissesRound()
        False
        >>> card1.setSymbol("Q")
        >>> card2.setSymbol(5)
        >>> player.setFirstCard(card1)
        >>> player.setSecCard(card2)
        >>> player.checkNextMissesRound()
        False
        """
        if (self.getFirstCard().getSymbol() != "Q" and self.getSecCard().getSymbol() == "K"):
            print("You picked 2 Ks, so the next player loses their round.")
            return True
        else:
            return False


    def checkForThirdCard(self):
        """
        >>> from card import *
        >>> player = Player()
        >>> card1 = Card()
        >>> card1.setSymbol("Q")
        >>> card2 = Card()
        >>> card2.setSymbol("K")
        >>> player.setFirstCard(card1)
        >>> player.setSecCard(card2)
        >>> player.checkForThirdCard()
        You picked a Q and a K, so you get to chose a third card.
        True
        >>> card1.setSymbol("J")
        >>> card2.setSymbol("K")
        >>> player.setFirstCard(card1)
        >>> player.setSecCard(card2)
        >>> player.checkForThirdCard()
        False
        >>> card1.setSymbol("Q")
        >>> card2.setSymbol(2)
        >>> player.setFirstCard(card1)
        >>> player.setSecCard(card2)
        >>> player.checkForThirdCard()
        False
        >>> card1.setSymbol("K")
        >>> card2.setSymbol(5)
        >>> player.setFirstCard(card1)
        >>> player.setSecCard(card2)
        >>> player.checkForThirdCard()
        False
        """
        if (self.getFirstCard().getSymbol() == "Q" and self.getSecCard().getSymbol() == "K"):
            print("You picked a Q and a K, so you get to chose a third card.")
            return True
        else:
            return False   


if __name__ == "__main__":
    import doctest
    doctest.testmod()