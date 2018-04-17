"""
Bestand met Vak klasse en lijsten Heuristieken

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

import csv

class Vak(object):
    """
    Klasse om een vak te representeren
    """
    def __init__(self, id, naam, hc, wc, maxWc, prac, maxPrac):
        self.id = id
        self.naam = naam
        self.hc = hc
        self.wc =  wc
        self.maxWc = maxWc
        self.prac = prac
        self.maxPrac = maxPrac
        self.aantalStudenten = 0
        self.studenten = []

    def __str__(self):
        return self.naam

# aanmaken van dict en vakkenlijst creëren    
counter = -1
vakkenLijst = []
vanVakNaarId = {}

# inlezen van CSV bestand
with open('vakken.csv') as csvFile:
    readCSV = csv.reader(csvFile, delimiter=';')

    # rijen van CSV inlezen en vakobject aanmaken
    for row in readCSV:
        if counter != -1:
            vakkenLijst.append(Vak(counter, row[0], row[1], row[2], row[3], row[4], row[5]))
            vanVakNaarId[row[0]] = counter
        counter += 1
csvFile.close()
