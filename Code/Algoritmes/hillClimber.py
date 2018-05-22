"""
Algoritme dat een rooster zoekt door allen wissels toe te staan die voor verbetering zorgen.

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

import random
import rooster as Rooster
import zaalSlot as ZaalSlot

def hillClimbing(rooster):

    minIteraties = 2000
    mutaties = 0
    lijstScore = []

    score = rooster.score()

    for i in range(minIteraties):

        # wissel twee willekeurige zaalsloten
        indexZaalslot = random.sample(range(len(rooster.zaalslotenLijst)), 2)
        randomZaalslot1 = rooster.zaalslotenLijst[indexZaalslot[0]]
        randomZaalslot2 = rooster.zaalslotenLijst[indexZaalslot[1]]

        randomZaalslot1.wissel(randomZaalslot2)
        score2 = rooster.score()
        lijstScore.append(score)

        if score2 > score:
            score = score2
            mutaties += 1

        else:
            randomZaalslot2.wissel(randomZaalslot1)

    aantalIteraties = []
    for i in range(minIteraties):
        aantalIteraties.append(i)

    return [rooster, lijstScore]
