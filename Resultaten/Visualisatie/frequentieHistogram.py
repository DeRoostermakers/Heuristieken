"""
Functie om de verdeling van scores in te zien.

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

def frequentieHistogram(scoreLijst):

    # plot de bargrafiek
    ontwerp = go.Histogram(x=scoreLijst, xbins=dict(start=np.min(scoreLijst), size=10,
                           end=np.max(scoreLijst)), marker=dict(color='rgb(74, 102, 118)'))
    layout = go.Layout(title="Histogram met scorefrequentie")
    figuur = go.Figure(data=go.Data([ontwerp]), layout=layout)
    py.plot(figuur, filename='histogram-frequentie')

    # statistieken bekijken
    gemiddelde = np.mean(scoreLijst)
    afwijking = np.std(scoreLijst)
    mediaan = np.median(scoreLijst)
    maximum = np.max(scoreLijst)
    minimum = np.min(scoreLijst)

    print("Het gemiddelde is " + str(gemiddelde))
    print("De standaardafwijking is " + str(afwijking))
    print("De mediaan is " + str(mediaan))
    print("Het maximum is " + str(maximum))
    print("Het minimum is " + str(minimum))
