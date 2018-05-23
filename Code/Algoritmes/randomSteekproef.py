"""
Functie om de verdeling van scores in te zien middels random sampling.

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

def randomSteekproef(rooster, iteraties):

    # simuleer aantal iteraties keer het rooster en onthoud scores
    scores = []
    for simulatie in range(1, iteraties + 1):
        rooster.vulRandom()
        scores.append(rooster.score())

    # plot de bargrafiek
    ontwerp = go.Histogram(x=scores, xbins=dict(start=np.min(scores), size=20,
                           end=np.max(scores)), marker=dict(color='rgb(74, 102, 118)'))
    layout = go.Layout(title="Histogram met scorefrequentie")
    figuur = go.Figure(data=go.Data([ontwerp]), layout=layout)
    py.plot(figuur, filename='histogram-frequentie')

    # statistieken bekijken
    gemiddelde = np.mean(scores)
    afwijking = np.std(scores)
    mediaan = np.median(scores)
    maximum = np.max(scores)
    minimum = np.min(scores)

    print("Het gemiddelde is " + str(gemiddelde))
    print("De standaardafwijking is " + str(afwijking))
    print("De mediaan is " + str(mediaan))
    print("Het maximum is " + str(maximum))
    print("Het minimum is " + str(minimum))
