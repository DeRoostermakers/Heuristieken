"""
Bestand met Activiteit klasse en lijsten Heuristieken

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

class Activiteit(object):
    """
    Klasse om een activiteit te representeren
    """

    def __init__(self, groepnr, soort, vakId, maxStud, nrStud, welkeStud):
        self.groepnr = groepnr
        self.soort = soort
        self.vakId = vakId
        self.maxStud = maxStud
        self.nrStud = nrStud
        self.welkeStud = welkeStud
        self.dag = 0
        self.tijdslot = 0
        self.activiteitId = str(self.vakId) + "." + str(self.soort) + "." + str(self.groepnr)

    def __str__(self):
        return self.activiteitId + str(self.dag) + str(self.tijdslot)

    def __repr__(self):
        return self.activiteitId + str(self.dag) + str(self.tijdslot)
