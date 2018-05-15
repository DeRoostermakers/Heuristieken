"""
Algoritme dat een rooster zoekt door recombinatie en mutatie.

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

import random
import rooster as Rooster
import zaalSlot as ZaalSlot
import copy
#import plotly.plotly as py
#import plotly.graph_objs as go
#import numpy as np

def hillClimbing(dagen, tijdsloten):
    # maak een rooster object aan
    rooster = Rooster.Rooster(dagen, tijdsloten)
    minIteraties = 3000
    score = 0
    rooster.vulRandom()
    score = rooster.score()

    mutaties = 0
    lijstScore = []
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
            # print(score)

        else:
            randomZaalslot2.wissel(randomZaalslot1)


    print(lijstScore)


    # trace = go.Scatter(
    #     x = random_x,
    #     y = random_y
    # )
    #
    # data = [trace]
    #
    # py.iplot(data, filename='basic-line')
