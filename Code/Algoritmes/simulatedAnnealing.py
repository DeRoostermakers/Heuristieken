"""
Algoritme dat een rooster zoekt door recombinatie en mutatie.

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

import random
import math
import zaalSlot as ZaalSlot

def simulatedAnnealing(rooster, minIteraties):

    # definieer temperaturen
    beginTemperatuur = 100
    eindTemperatuur = 1

    # initialiseer variabelen
    score = rooster.score()
    mutaties = 0
    lijstScore = []
    simulatedAnnealingRooster = []
    for i in range(minIteraties):

        # wissel twee willekeurige zaalsloten
        indexZaalslot = random.sample(range(len(rooster.zaalslotenLijst)), 2)
        randomZaalslot1 = rooster.zaalslotenLijst[indexZaalslot[0]]
        randomZaalslot2 = rooster.zaalslotenLijst[indexZaalslot[1]]
        randomZaalslot1.wissel(randomZaalslot2)
        score2 = rooster.score()
        lijstScore.append(score)

        # bereken temperatuur en acceptatiekans
        # lineair
        temperatuur = beginTemperatuur - i * (beginTemperatuur - eindTemperatuur) / minIteraties
        # # exponentieel
        # temperatuur = beginTemperatuur * (eindTemperatuur / beginTemperatuur)^(i / minIteraties)
        # # sigmoidal
        # temperatuur = eindTemperatuur + (beginTemperatuur - eindTemperatuur) / (1 + math.exp(0.3 * (i - minIteraties / 2)))

        verkorting = score2 - score
        acceptatieKans = math.exp(verkorting/temperatuur)

        # accepteer verandering als score verbeterd
        if acceptatieKans >= 1:
            score = score2
            mutaties += 1

        # accepteer slechtere score afhankelijk van acceptatiekans
        elif acceptatieKans < 1:

            # nog steeds geaccepteerd toegestaan
            nummer = random.random()
            if acceptatieKans > nummer:
                score = score2
                mutaties += 1

            # niet geaccepteerd
            else:
                randomZaalslot2.wissel(randomZaalslot1)

    simulatedAnnealingRooster.append([rooster, score])

    # print(aantalIteraties)
    print(lijstScore)
    return rooster
