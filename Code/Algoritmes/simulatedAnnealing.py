"""
Algoritme dat een verbetering van de score zoekt door willekeuroge zaalsloten te wisselen
en een verslechtering van een oplossing toelaat aan de hand van een koelschema

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

import random
import math
import zaalSlot as ZaalSlot
from willekeurigeWissel import willekeurigeWissel

def simulatedAnnealing(rooster, minIteraties, beginTemperatuur, eindTemperatuur, temperatuurFunctie):

    # initialiseer variabelen
    score = rooster.score()
    scoreLijst = []
    scoreLijst.append(score)

    for i in range(minIteraties):

        # wissel twee willekeurige zaalsloten
        randomZaalslot1, randomZaalslot2 = willekeurigeWissel(rooster.zaalslotenLijst)
        randomZaalslot1.wissel(randomZaalslot2)
        score2 = rooster.score()

        # bereken temperatuur en acceptatiekans
        temperatuur = temperatuurFunctie(beginTemperatuur, eindTemperatuur, minIteraties, i)
        verkorting = score2 - score
        acceptatieKans = math.exp(verkorting / temperatuur)

        # accepteer verandering als score verbetert
        if acceptatieKans >= 1:
            score = score2

        # accepteer slechtere score afhankelijk van acceptatiekans
        elif acceptatieKans < 1:
            nummer = random.random()
            if acceptatieKans > nummer:
                score = score2
            else:
                randomZaalslot2.wissel(randomZaalslot1)

        # documenteer de verbetering van de score
        scoreLijst.append(score)

    return rooster, scoreLijst

def lineairFunctie(beginTemperatuur, eindTemperatuur, minIteraties, i):
    " Berekent temperatuur aan de hand van lineaire formule "

    temperatuur = beginTemperatuur - i * (beginTemperatuur - eindTemperatuur) / minIteraties
    return temperatuur

def exponentieelFunctie(beginTemperatuur, eindTemperatuur, minIteraties, i):
    " Berekent temperatuur aan de hand van exponentiële formule "

    temperatuur = beginTemperatuur * math.pow((eindTemperatuur / beginTemperatuur), (i / minIteraties))
    return temperatuur

def sigmoidalFunctie(beginTemperatuur, eindTemperatuur, minIteraties, i):
    " Berekent temperatuur aan de hand van sigmoidale formule "

    temperatuur = eindTemperatuur + (beginTemperatuur - eindTemperatuur) / (1 + math.exp(0.3 * (i - minIteraties / 2)))
    return temperatuur
