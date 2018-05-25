"""
Algoritme dat een rooster zoekt door alle willekeurige wissels toe te staan die voor verbetering zorgen

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

import zaalSlot as ZaalSlot
from willekeurigeWissel import willekeurigeWissel

def hillClimberStochastisch(rooster, minIteraties):

    # initialiseer variabelen
    scoreLijst = []
    score = rooster.score()
    scoreLijst.append(score)
    for i in range(minIteraties):

        # wissel twee willekeurige zaalsloten
        randomZaalslot1, randomZaalslot2 = willekeurigeWissel(rooster.zaalslotenLijst)
        randomZaalslot1.wissel(randomZaalslot2)
        score2 = rooster.score()

        # accepteer wissel als de score verbetert
        if score2 > score:
            score = score2

        # behoud oude rooster als wissel geen verbetering geeft
        else:
            randomZaalslot2.wissel(randomZaalslot1)

        # documenteer de verbetering van de score
        scoreLijst.append(score)

    return rooster, scoreLijst
