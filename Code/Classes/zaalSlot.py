"""
Zaalslot klasse

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

class ZaalSlot(object):

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
        " Wissel twee activiteiten van tijdslot "

        # sla de eerste activiteit tijdelijk op
        tijdelijkDag = self.dag
        tijdelijkTijdslot = self.tijdslot


        # sla de twee activiteit informatie op
        self.activiteit.dag = zaalslot.dag
        self.activiteit.tijdslot = zaalslot.tijdslot

        zaalslot.activiteit.dag = tijdelijkDag
        zaalslot.activiteit.tijdslot = tijdelijkTijdslot

        tijdelijkActiviteit = self.activiteit

        self.activiteit = zaalslot.activiteit
        zaalslot.activiteit = tijdelijkActiviteit



    def voegToe(self, activiteit):
        " Voeg een activiteit aan een zaalslot toe "

        # voeg activiteit aan het zaalslot toe
        self.activiteit = activiteit
        self.inGebruik = 1
        activiteit.dag = self.dag
        activiteit.tijdslot = self.tijdslot
