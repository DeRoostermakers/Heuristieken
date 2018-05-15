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
    minIteraties = 0
    score = 0
    rooster.vulRandom()
    score = rooster.score()
    print(score)


    # wissel twee willekeurige zaalsloten
    indexZaalslot = random.sample(range(len(rooster.zaalslotenLijst)), 2)
    randomZaalslot1 = rooster.zaalslotenLijst[indexZaalslot[0]]
    randomZaalslot2 = rooster.zaalslotenLijst[indexZaalslot[1]]
    randomZaalslot1.wissel(randomZaalslot2)
    score = rooster.score()
    print(score)
