"""
Bestand met Vak klasse en lijsten Heuristieken

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

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

    def __repr__(self):
        return self.naam

