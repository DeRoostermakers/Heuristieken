"""
Algoritme dat een rooster zoekt door recombinatie en mutatie.

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

import random
import rooster as Rooster
import zaalSlot as ZaalSlot


def simulatedAnneling(dagen, tijdsloten):
    # maak een rooster object aan
    rooster = Rooster.Rooster(dagen, tijdsloten)
    minIteraties = 2000
    rooster.vulRandom()
    score = rooster.score()


    acceptatieKans = math.exp(1)
    print(acceptatieKans)


    #
    # mutaties = 0
    # lijstScore = []
    # simulatedAnnelingRooster = []
    # for i in range(minIteraties):
    #
    #     # wissel twee willekeurige zaalsloten
    #     indexZaalslot = random.sample(range(len(rooster.zaalslotenLijst)), 2)
    #     randomZaalslot1 = rooster.zaalslotenLijst[indexZaalslot[0]]
    #     randomZaalslot2 = rooster.zaalslotenLijst[indexZaalslot[1]]
    #     randomZaalslot1.wissel(randomZaalslot2)
    #     score2 = rooster.score()
    #     lijstScore.append(score)
    #
    #     if score2 > score:
    #         score = score2
    #         mutaties += 1
    #
    #     else:
    #         # nog steeds geaccepteerd toegestaan
    #
    #         # niet geaccepteerd
    #         randomZaalslot2.wissel(randomZaalslot1)
    #
    # simulatedAnnelingRooster.append([rooster, score])
    #
    # aantalIteraties = []
    # for i in range(minIteraties):
    #     aantalIteraties.append(i)
    #
    # # print(aantalIteraties)
    # # print(lijstScore)
    # print(simulatedAnnelingRooster)
    # return simulatedAnnelingRooster
