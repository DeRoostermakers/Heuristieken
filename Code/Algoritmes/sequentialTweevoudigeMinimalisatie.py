"""
Algoritme dat een leeg rooster invult aan de hand van de zaalgroottes.
LET OP: dit algoritme kan alleen op een leeg rooster worden gebruikt

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

import random
import rooster as Rooster
import math
from willekeurigeWissel import willekeurigeWissel
from iteratieVisualisatie import iteratieVisualisatie
from sequentialEenvoudigeMinimalisatie import sequentialEenvoudigeMinimalisatie

def sequentialTweevoudigeMinimalisatie(rooster, minIteraties, verschil):

    # deel het rooster in via zaalgrootte
    sequentialRooster = sequentialEenvoudigeMinimalisatie(rooster)[0]

    print("score na sequential: " + str(sequentialRooster.score()))

    zalen = []
    zalenTemp = []
    scoreLijst = []

    # sorteer de zaalsloten op het aantal studenten per capaciteit
    sequentialRooster.zaalslotenLijst.sort(key = lambda x: x.capaciteit, reverse = True)

    # voeg het eerste zaalslot toe
    zalenTemp.append(sequentialRooster.zaalslotenLijst[0])

    # groepeer de zaalsloten op een bepaald grootte verschil
    for i in range(len(sequentialRooster.zaalslotenLijst)):
        if sequentialRooster.zaalslotenLijst[i - 1].capaciteit - sequentialRooster.zaalslotenLijst[i].capaciteit > verschil:
            zalen.append(zalenTemp)
            zalenTemp = []
            zalenTemp.append(sequentialRooster.zaalslotenLijst[i])
        else:
            zalenTemp.append(sequentialRooster.zaalslotenLijst[i])

    for zaal in zalen:
        score = rooster.score()
        for i in range(minIteraties):

            # wissel twee willekeurige zaalsloten
            randomZaalslot1, randomZaalslot2 = willekeurigeWissel(sequentialRooster.zaalslotenLijst)
            randomZaalslot1.wissel(randomZaalslot2)
            score2 = sequentialRooster.score()

            if score2 > score:
                score = score2

            else:
                randomZaalslot2.wissel(randomZaalslot1)
            scoreLijst.append(sequentialRooster.score())

    print("score na hillclimber : " + str(sequentialRooster.score()))

    return sequentialRooster, scoreLijst
