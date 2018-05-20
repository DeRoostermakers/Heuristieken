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
    minIteraties = 15000
    rooster.vulRandom()
    score = rooster.score()

    print(str(rooster.activiteitenLijst[1]))
    print(str(rooster.activiteitenLijst[2]))

<<<<<<< HEAD
    ID1 = rooster.activiteitenLijst[1].activiteitId
    ID2 = rooster.activiteitenLijst[2].activiteitId

    zaalslot1 = rooster.zaalslotenLijst[1]
    zaalslot2 = rooster.zaalslotenLijst[2]

    for zaalslot in rooster.zaalslotenLijst:
        if zaalslot.activiteit.activiteitId == ID1:
            zaalslot1 = zaalslot
        elif zaalslot.activiteit.activiteitId == ID2:
            zaalslot2 = zaalslot

    zaalslot1.wissel(zaalslot2)

    print(str(rooster.activiteitenLijst[1]))
    print(str(rooster.activiteitenLijst[2]))
=======
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
            print(score2)
        else:
            randomZaalslot2.wissel(randomZaalslot1)

    hillClimberRooster.extend([rooster, score])
>>>>>>> 83a1bd74925769d8d2eb71fcdb133b30388a45ac


    # mutaties = 0
    # lijstScore = []
    # hillClimberRooster = []
    # for i in range(minIteraties):
    #
    #     # wissel twee willekeurige zaalsloten
    #     indexZaalslot = random.sample(range(len(rooster.zaalslotenLijst)), 2)
    #     randomZaalslot1 = rooster.zaalslotenLijst[indexZaalslot[0]]
    #     randomZaalslot2 = rooster.zaalslotenLijst[indexZaalslot[1]]
    #
    #     randomZaalslot1.wissel(randomZaalslot2)
    #     score2 = rooster.score()
    #     lijstScore.append(score)
    #     input()
    #
    #     if score2 > score:
    #         score = score2
    #         mutaties += 1
    #
    #     else:
    #         randomZaalslot2.wissel(randomZaalslot1)
    #
    # hillClimberRooster.append([rooster, score])
    #
    # aantalIteraties = []
    # for i in range(minIteraties):
    #     aantalIteraties.append(i)

    # print(lijstScore)


    # print(aantalIteraties)
    # print(lijstScore)
    # print(hillClimberRooster)
    # return hillClimberRooster
