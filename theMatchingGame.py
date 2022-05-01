from inOut import getInputs
from playerHelper import *
from deck import *
from player import *

def main():
    #Sets the game.
    #Gets the game's settings from the user, and creates the appropriate players list and deck.
    playersNum, difLvl = getInputs()
    players = createPlayers(playersNum)
    deck = Deck()
    deck.createDeck(difLvl)

    #Shows the deck once before the game starts.
    deck.print()

    #Starts the game.
    deck.printHidden()

    currentPlayer = 0
    while True:     
        #Current player gets their round(s).
        players[currentPlayer].playRound(deck)
        while (players[currentPlayer].getPlayAgainFlag() == True):
            players[currentPlayer].playRound(deck)

        #Checks if the game is over, in which case the loop is broken.
        if (deck.hasClosedCards() == False):
            break

        #Sets the next player. 
        #Checks if the next player must lose their round, and if the players list must be reset.
        elif (players[currentPlayer].getNextMissesFlag() == False):
            currentPlayer = currentPlayer + 1
            if (currentPlayer == int(playersNum)):
                currentPlayer = 0
        elif (players[currentPlayer].getNextMissesFlag() == True):
            if (int(playersNum) == 2):
                pass 
            else:
                if (currentPlayer + 2 <= int(playersNum) - 1):
                    currentPlayer = currentPlayer + 2  
                elif (currentPlayer + 2 == int(playersNum)):
                    currentPlayer = 0
                elif (currentPlayer + 2 > int(playersNum)):
                    currentPlayer = 1


    #After game results.
    winner, tied = findBestPlayer(players)
    if tied == 0:
        print ("The game is over! Player", int(winner.getName()) + 1, "is the winner with", winner.getPoints(), "point(s).")
    else:
        print ("The game is over! Players", int(winner.getName()) + 1, "and", int(tied.getName()) + 1, "tied with", winner.getPoints(), "point(s).")


if __name__ == "__main__":
    main()