import random

pups = ["B","O","G","R","P","Y"]
spinner = ["B","O","G","R","P","Y"]
gameBoard = ["Y","B","O","YSI","G","R","P","Y","BSI","B","YSO","O","G","R","P","Y","BSO","B","O","G","R","P","OSI","Y","B","O","G","R","OSO","P","Y","B","O","GSI","G","R","P","Y","PSI","B","GSO","O","G","R","P","PSO","Y","B","O","G","R","P","Y","RSI","B","O","G","R","P","RSO","Y","B","O","G","R","P","END"]

def playOneGame(debug = False, pickedPup = "", pickedSpins = []):
    if pickedPup == "":
        pup = random.choice(pups)
    else:
        pup = pickedPup

    if debug:
        print("Playing as " + pup)
    badges = []
    badges.append(pup)
    currentSpot = -1
    currentPickedSpin = 0
    gameLog = []
    gameOver = False
    while not gameOver:
        if len(pickedSpins) == 0:
            spin = random.choice(spinner)
        else:
            if currentPickedSpin == len(pickedSpins):
                currentPickedSpin = len(pickedSpins) -1
            spin = pickedSpins[currentPickedSpin]
            currentPickedSpin = currentPickedSpin + 1
        if debug:
            print("Spin was " + spin)
        gameLog.append(spin)
        if not spin in badges:
            if debug:
                print("Gained Badge " + spin)
            badges.append(spin)
        while True:
            currentSpot = currentSpot + 1
            if debug:
                print ("Moving to Spot " + str(currentSpot))
            if "SI" in gameBoard[currentSpot]:
                if gameBoard[currentSpot][0] in badges:
                    currentShortCut = gameBoard[currentSpot][0]
                    if debug:
                        print("Taking " + currentShortCut + " shortcut")
                    while True:
                        currentSpot = currentSpot + 1
                        if debug:
                            print ("Moving to Spot " + str(currentSpot))
                        if (gameBoard[currentSpot] == currentShortCut + "SO"):
                            if debug:
                                print("Ending " + currentShortCut + " shortcut")
                            break
            if gameBoard[currentSpot] == "END":
                gameOver = True
            if gameBoard[currentSpot] == spin or gameOver:
                break
                
        
    if debug:
        print("Number of Moves: " + str(len(gameLog)))
    return pup,gameLog

#maxMoves = len(gameBoard) - 40
maxMoves = 17

shortestWin = maxMoves
numberOfShortestWins = 0
longestWin = 0
numberOfLongestWins = 0
longestMoves = []
shortestMoves = []
 
totalGames = maxMoves **6 * 6

#playOneGame(True,"B",["Y","B","G","P","B","B","O","O","O","O","O","O","O"])

for x in range(6):
    print("Trying " + pups[x] + " Games.")
    for games in range(maxMoves ** 6):
        if totalGames % 10000 == 0:
            print("Only " + str(totalGames) + " to go!")
        moveList = []
        #for y in range(maxMoves):
        #    moveList.append(spinner[((games // 6 ** (y) % 6))])
       
        currentPup, currentGameLog = playOneGame(False, pups[x], moveList)

        if (len(currentGameLog) < shortestWin):
            shortestWin = len(currentGameLog)
            numberOfShortestWins = 1
            shortestMoves = []
            shortestMoves.append([pups[x],currentGameLog])

        if (len(currentGameLog) == shortestWin):
            if [pups[x],currentGameLog] not in shortestMoves:
             numberOfShortestWins = numberOfShortestWins +1
             shortestMoves.append([pups[x],currentGameLog])

        if (len(currentGameLog) > longestWin):
            longestWin = len(currentGameLog)
            numberOfLongestWins = 1
            longestMoves = []
            longestMoves.append([pups[x],currentGameLog])

        if (len(currentGameLog) == longestWin):
            if [pups[x],currentGameLog] not in longestMoves:
                numberOfLongestWins = numberOfLongestWins + 1
                longestMoves.append([pups[x],currentGameLog])

        totalGames = totalGames -1


print("Shortest Moves: " + str(shortestWin) + " and there are " + str(numberOfShortestWins) + " of them.")
print("Example: Pup: " + shortestMoves[0][0] + " with moves: ")
print(*shortestMoves[0][1])
print("Longest Moves: " + str(longestWin) + " and there are " + str(numberOfLongestWins) + " of them.")
print("Example: Pup: " + longestMoves[0][0] + " with moves: ")
print(*longestMoves[0][1])
    
print("")
for game in shortestMoves:
    print (game[0])
    print (*game[1])





# Only 30000 to go!
# Only 20000 to go!
# Only 10000 to go!
# Shortest Moves: 6 and there are 18 of them.
# Example: Pup: B with moves:
# R G O B B B
# Longest Moves: 23 and there are 13 of them.
# Example: Pup: O with moves:
# O O G R P Y B O G R Y B O O R O G P O G R P G

# B
# R G O B B B
# B
# P R O O B Y
# B
# P R O O O O
# B
# P R O B B Y
# B
# P R O O O Y
# B
# P R O B B B
# B
# P R O O B B
# B
# R G O B B Y
# B
# P R O O O B
# Y
# P R O O O Y
# Y
# P R O B B B
# Y
# P R O B B Y
# Y
# P R O O B Y
# Y
# P R O O O B
# Y
# P R O O O O
# Y
# R G O B B Y
# Y
# R G O B B B
# Y
# P R O O B B