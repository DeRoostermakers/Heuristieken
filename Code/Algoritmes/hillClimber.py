"""
Algoritme dat een rooster zoekt door recombinatie en mutatie.

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

import random
import rooster as Rooster
import zaalSlot as ZaalSlot

def hillClimbing(dagen, tijdsloten):
    # maak een rooster object aan
    rooster = Rooster.Rooster(dagen, tijdsloten)
    minIteraties = 1000
    score = 0
    rooster.vulRandom()
    score = rooster.score()
    
    nieuwRooster = rooster
    mutaties = 0
    lijstScore = []
    for i in range(minIteraties):

        # wissel twee willekeurige zaalsloten
        indexZaalslot = random.sample(range(len(nieuwRooster.zaalslotenLijst)), 2)
        randomZaalslot1 = nieuwRooster.zaalslotenLijst[indexZaalslot[0]]
        randomZaalslot2 = nieuwRooster.zaalslotenLijst[indexZaalslot[1]]
        randomZaalslot1.wissel(randomZaalslot2)
        score2 = nieuwRooster.score()
        lijstScore.append(score)

        if score2 > score:
            rooster = nieuwRooster
            score = score2
            mutaties += 1
            # print(score)

    print(lijstScore)
