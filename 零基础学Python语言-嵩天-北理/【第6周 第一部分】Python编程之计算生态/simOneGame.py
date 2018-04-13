import random
def simOneGame():
    scoreA = 0
    scoreB = 0
    serving = "A"
    for i in range(30):    
        if serving == "A":
            if random.random() < 0.5:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random.random() < 0.5:
                scoreB = scoreB + 1
            else:
                serving = "A"
    print(scoreA)
    print(scoreB)