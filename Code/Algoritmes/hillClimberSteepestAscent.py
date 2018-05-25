"""
Algoritme dat een rooster zoekt door alle mogelijke wissels van een activiteit
te bekijken en de beste wissel te accepteren

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

import random
import zaalSlot as ZaalSlot
from operator import itemgetter

def hillClimberSteepestAscent(rooster, minIteraties):

    # initialiseer variabelen
    scoreLijst = []
    score = rooster.score()
    scoreLijst.append(score)
    stop = 0

    # initialiseer variabelen
    for i in range(minIteraties):
        if stop > 50:
            break
        scoreAlleWissels = []

        # selecteer een willekeurig zaalslot
        indexZaalslot = random.sample(range(len(rooster.zaalslotenLijst)), 1)

        # controleer elke mogelijke wissel met zaalslot
        for j in range(len(rooster.zaalslotenLijst)):
            if j != indexZaalslot[0]:
                randomZaalslot1 = rooster.zaalslotenLijst[indexZaalslot[0]]
                randomZaalslot2 = rooster.zaalslotenLijst[j]
                randomZaalslot1.wissel(randomZaalslot2)
                score2 = rooster.score()

                # accepteer wissel als de score verbetert
                if score2 > score:
                    score = score2
                else:
                    randomZaalslot2.wissel(randomZaalslot1)

        # documenteer de verbetering van de score
        scoreLijst.append(score)

    return rooster, scoreLijst
