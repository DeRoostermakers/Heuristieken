"""
Algoritme dat een rooster zoekt door allen wissels toe te staan die voor verbetering zorgen.

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

import random
import rooster as Rooster
import zaalSlot as ZaalSlot


def hillClimbing(dagen, tijdsloten):
    # maak een rooster object aan
    rooster = Rooster.Rooster(dagen, tijdsloten)
    minIteraties = 100
    rooster.vulRandom()
    score = rooster.score()

    mutaties = 0
    lijstScore = []
    hillClimberRooster = []
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

    hillClimberRooster.append([rooster, score])

    aantalIteraties = []
    for i in range(minIteraties):
        aantalIteraties.append(i)

    # print(lijstScore)


    # print(aantalIteraties)
<<<<<<< HEAD
    print(lijstScore)
    # print(hillClimberRooster)
    return hillClimberRooster
=======
    # print(lijstScore)
    print(hillClimberRooster)
    return rooster
>>>>>>> 924a87290306d2bac03670ff016e149efceabf4e
