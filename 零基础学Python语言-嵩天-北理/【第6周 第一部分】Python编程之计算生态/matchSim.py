#matchSim.py
from random import * 
 
def main():
    printIntro()
    probA,probB,n = getInputs()
    winsA, winsB = simNGames(n,probA,probB)
    PrintSummary(winsA, winsB)
 
def printIntro():
    print('This program simulates a game between two')
    print('There are two players, A and B')
    print('Probability(a number between 0 and 1)is used')
 
def getInputs():
    a = eval(input('What is the prob.player A wins?'))
    b = eval(input('What is the prob.player B wins?'))
    n = eval(input('How many games to simulate?'))
    return a,b,n
 
def simNGames(n,probA,probB):
    winsA = 0
    winsB = 0
    for i in range(n):
        scoreA,scoreB = simOneGame(probA,probB)
        if scoreA >scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA,winsB
def simOneGame(probA,probB):
    scoreA = 0
    scoreB = 0
    serving = "A"
    while not gameOver(scoreA,scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA,scoreB
 
def gameOver(a,b):
    return a==15 or b==15
 
def PrintSummary(winsA, winsB):
    n = winsA + winsB
    print('\nGames simulated:%d'%n)
    print('Wins for A:{0}({1:0.1%})'.format(winsA,winsA/n))
    print('Wins for B:{0}({1:0.1%})'.format(winsB,winsB/n))
 
if __name__ == '__main__':
    main()