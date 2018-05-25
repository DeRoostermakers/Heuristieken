"""
Algoritme dat een rooster zoekt door alle wissels toe te staan die voor verbetering zorgen

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

import random

def willekeurigeWissel(zaalslotenLijst):

    # neem 2 willekeurige activiteiten en wissel deze
    indexZaalslot = random.sample(range(len(zaalslotenLijst)), 2)
    randomZaalslot1 = zaalslotenLijst[indexZaalslot[0]]
    randomZaalslot2 = zaalslotenLijst[indexZaalslot[1]]

    return randomZaalslot1, randomZaalslot2
