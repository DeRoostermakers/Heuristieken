"""
Bestand met Zaal klasse en lijsten Heuristieken

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

class Zaal(object):
    """
    Klasse om een zaal te representeren
    """

    def __init__(self, naam, capaciteit):
        self.naam = naam
        self.capaciteit = capaciteit
        self.inGebruik = 0
        self.activiteit = None

    def __str__(self):
        return self.naam

    def __repr__(self):
        return self.naam
