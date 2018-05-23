"""
Algoritme dat een rooster zoekt door allen wissels toe te staan die voor verbetering zorgen.

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

import zaalSlot as ZaalSlot
from willekeurigeWissel import willekeurigeWissel

def hillClimber(rooster, minIteraties):

    scoreLijst = []
    score = rooster.score()

    for i in range(minIteraties):

        # wissel twee willekeurige zaalsloten
        randomZaalslot1, randomZaalslot2 = willekeurigeWissel(rooster.zaalslotenLijst)
        randomZaalslot1.wissel(randomZaalslot2)
        score2 = rooster.score()
        scoreLijst.append(score)

        if score2 > score:
            score = score2

        else:
            randomZaalslot2.wissel(randomZaalslot1)

    return rooster, scoreLijst
