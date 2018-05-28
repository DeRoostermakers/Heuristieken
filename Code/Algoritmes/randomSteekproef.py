"""
Algoritme die een bepaald aantal keer een willekeurig rooster uit de
toestandsruimte trekt

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

def randomSteekproef(rooster, iteraties):

    # trek iteraties keer een willekeurig rooster uit de toestandsruimte
    scoreLijst = []
    for simulatie in range(1, iteraties + 1):
        rooster.vulRandom()
        scoreLijst.append(rooster.score())

    return rooster, scoreLijst
