"""
Algoritme dat een rooster zoekt door recombinatie en mutatie.

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

import random

def hillClimbing(rooster):
    minIteraties = 0
    score = 0
    rooster.vulRandom()
    scores = rooster.score()
    
    print("scores")
