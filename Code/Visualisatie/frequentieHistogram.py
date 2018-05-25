"""
Functie om de frequentieverdeling van scores weer te geven

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

import plotly as py
import plotly.graph_objs as go
import numpy as np
from plotly import tools
py.tools.set_credentials_file(username = "DeRoostermakers", api_key = "kMZnofKi6pSyYy6Ih1bI")

def frequentieHistogram(scoreLijst):

    # plot de bargrafiek
    ontwerp = go.Histogram(x = scoreLijst, xbins = dict(start = np.min(scoreLijst), size = 20,
                           end = np.max(scoreLijst)), marker = dict(color="rgb(74, 102, 118)"))
    layout = go.Layout(title = "Histogram met scorefrequentie")
    figuur = go.Figure(data = go.Data([ontwerp]), layout = layout)
    py.plotly.plot(figuur, filename = "Frequentiehistogram")

    # berekenen de statistieken
    gemiddelde = np.mean(scoreLijst)
    afwijking = np.std(scoreLijst)
    mediaan = np.median(scoreLijst)
    maximum = np.max(scoreLijst)
    minimum = np.min(scoreLijst)

    # geef de statistieken weer
    print("Het gemiddelde is " + str(gemiddelde))
    print("De standaardafwijking is " + str(afwijking))
    print("De mediaan is " + str(mediaan))
    print("Het maximum is " + str(maximum))
    print("Het minimum is " + str(minimum))
