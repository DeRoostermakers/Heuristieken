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

def eenvoudigeMinimalisatie(rooster):
    scoreLijst = []
    legeActiviteiten = []

    # maak een random volgorde van de zaalslotenlijst
    random.shuffle(rooster.zaalslotenLijst, random.random)

    # maak een random volgorde van de activiteitenlijst
    random.shuffle(rooster.activiteitenLijst, random.random)

    # sorteer de activiteiten op het aantal studenten per activiteit
    rooster.activiteitenLijst.sort(key = lambda x: x.nrStud, reverse = True)

    # sorteer de zaalsloten op het aantal studenten per capaciteit
    rooster.zaalslotenLijst.sort(key = lambda x: x.capaciteit, reverse = True)

    j = 0
    # voeg de activiteiten toe aan de zaalsloten, sla de zaalsloten van 17.00-19.00 en "lege activiteiten" over
    for activiteit in rooster.activiteitenLijst:
        if(activiteit.nrStud == 0):
            legeActiviteiten.append(activiteit)
            continue
        while(rooster.zaalslotenLijst[j].tijdslot == 5):
            j += 1

        rooster.zaalslotenLijst[j].voegToe(activiteit)
        j += 1

    k = 0
    # voeg de "lege activiteiten" aan de resterende zaalsloten toe
    for zaalslot in rooster.zaalslotenLijst:
        if zaalslot.inGebruik == 0:
            zaalslot.voegToe(legeActiviteiten[k])
            k += 1

    scoreLijst.append(rooster.score())
    return rooster, scoreLijst
