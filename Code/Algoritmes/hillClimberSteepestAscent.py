"""
Algoritme dat een rooster zoekt door allen wissels toe te staan die voor verbetering zorgen.

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

import random
from operator import itemgetter
import zaalSlot as ZaalSlot

def hillClimberSteepestAscent(rooster, minIteraties):

    # maak een rooster object aan
    score = rooster.score()
    scoreLijst = []
    scoreLijst.append(score)
    stop = 0
    for i in range(minIteraties):
        if stop > 50:
            break
        scoreAlleWissels = []

        # wissel twee willekeurige zaalsloten
        indexZaalslot = random.sample(range(len(rooster.zaalslotenLijst)), 1)
        for j in range(len(rooster.zaalslotenLijst)):
            if j != indexZaalslot[0]:
                randomZaalslot1 = rooster.zaalslotenLijst[indexZaalslot[0]]
                randomZaalslot2 = rooster.zaalslotenLijst[j]
                randomZaalslot1.wissel(randomZaalslot2)
                score2 = rooster.score()
                if score2 > score:
                    score = score2
                else:
                    randomZaalslot2.wissel(randomZaalslot1)
                print(score)

        # scoreGesorteerd = sorted(scoreAlleWissels, key=itemgetter(1), reverse=True)
        # score2 = scoreGesorteerd[0][1]

        # if score2 > score:
        #     score = score2
        #     stop = 0
        #
        # else:
        #     stop += 1

        scoreLijst.append(score)

    print(scoreLijst)
    return rooster, scoreLijst
