from player import *

#Creates the players list after the user provides the number of players
def createPlayers(plNum):
    players = []
    for i in range (int(plNum)):
        newPlayer = Player()
        newPlayer.setName(str(i))
        players.append(newPlayer)
    return players     

def findBestPlayer(players):
    best = players[0]
    tie = 0
    for i in range (1, len(players)):
        if (players[i].getPoints() > best.getPoints()):
            best = players[i]
        elif (players[i].getPoints() == best.getPoints()):
            tie = players[i]
    return best, tie