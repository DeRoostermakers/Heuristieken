"""
Functie die de scoreverbetering ten opzichte van de iteraties visualiseert.

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

import matplotlib.pyplot as plt

def iteratieVisualisatie(scoreLijst):

    iteratieLijst = []
    for i in range(len(scoreLijst)):
        iteratieLijst.append(i)

    plt.plot(iteratieLijst, scoreLijst)
    plt.title("Scoreverbetering t.o.v. iteraties")
    plt.xlabel("iteraties")
    plt.ylabel("score")
    plt.show()
