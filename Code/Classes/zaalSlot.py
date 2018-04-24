"""
Bestand met Zaal klasse en lijsten Heuristieken

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

class ZaalSlot(object):
    """
    Klasse om een zaalslot te representeren
    """

    def __init__(self, naam, capaciteit, dag, tijdslot):
        self.naam = naam
        self.capaciteit = capaciteit
        self.inGebruik = 0
        self.activiteit = None
        self.dag = dag
        self.tijdslot = tijdslot


    def __str__(self):
        return self.naam + "." + self.dag + "." + str(self.tijdslot) + "." + str(self.activiteit)

    def __repr__(self):
        return self.naam + "." + self.dag + "." + str(self.tijdslot) + "." + str(self.activiteit)
