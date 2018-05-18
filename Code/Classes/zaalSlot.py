"""
Bestand met Zaal klasse en lijsten Heuristieken

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

class ZaalSlot(object):
    """
    Klasse om een zaalslot te representeren
    """

    def __init__(self, naam, capaciteit, dag, tijdslot, idNaarDag):
        self.naam = naam
        self.capaciteit = capaciteit
        self.inGebruik = 0
        self.activiteit = None
        self.dag = dag
        self.tijdslot = tijdslot
        self.idNaarDag = idNaarDag
        self.zaalslotId = str(self.naam) + "." + str(self.dag) + "." + str(self.tijdslot)

    def __str__(self):
        return self.naam + "." + self.idNaarDag[self.dag] + "." + str(self.tijdslot) + "." + str(self.activiteit)

    def __repr__(self):
        return self.naam + "." + self.idNaarDag[self.dag] + "." + str(self.tijdslot) + "." + str(self.activiteit)

    def wissel(self, zaalslot):
        """ Wissel twee activiteiten van tijdslot"""

        # sla de eerste activiteit tijdelijk op
        # tijdelijkActiviteit = self.activiteit
        tijdelijkDag = self.dag
        tijdelijkTijdslot = self.tijdslot
        # tijdelijkInGebruik = self.inGebruik
        tijdelijkIdNaarDag = self.idNaarDag

        # verwissel de eerste activiteit met de tweede
        # self.activiteit = zaalslot.activiteit
        self.dag = zaalslot.dag
        self.tijdslot = zaalslot.tijdslot
        # self.inGebruik = zaalslot.inGebruik
        self.idNaarDag = zaalslot.idNaarDag

        if self.activiteit:
            self.activiteit.dag = zaalslot.dag
            self.activiteit.tijdslot = zaalslot.tijdslot

        # verwissel de tweede activiteit met de eerste
        # zaalslot.activiteit = tijdelijkActiviteit
        zaalslot.dag = tijdelijkDag
        zaalslot.tijdslot = tijdelijkTijdslot
        # zaalslot.inGebruik = tijdelijkInGebruik
        zaalslot.idNaarDag = tijdelijkIdNaarDag

        if zaalslot.activiteit:
            zaalslot.activiteit.dag = tijdelijkDag
            zaalslot.activiteit.tijdslot = tijdelijkTijdslot


    def voegToe(self, activiteit):
        """ Voeg een activiteit aan een zaalslot toe."""

        # voeg activiteit aan het zaalslot toe
        self.activiteit = activiteit
        self.inGebruik = 1
        activiteit.dag = self.dag
        activiteit.tijdslot = self.tijdslot
