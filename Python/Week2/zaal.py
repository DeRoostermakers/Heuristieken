
class Zaal(object):
    """
    Klasse om een zaal te representeren
    """

    def __init__(self, naam, capaciteit, inGebruik, vak):
        self.naam = naam
        self.capaciteit = capaciteit
        self.inGebruik = inGebruik
        self.vak = vak

    def __str__(self):
        return self.naam

    def __repr__(self):
        return self.naam

# initialiseer alle zalen
zaalLijst = []
zaalLijst.append(Zaal("A1.04", 41, 0, 0))
zaalLijst.append(Zaal("A1.06", 22, 0, 0))
zaalLijst.append(Zaal("A1.08", 20, 0, 0))
zaalLijst.append(Zaal("A1.10", 20, 0, 0))
zaalLijst.append(Zaal("B0.201", 56, 0, 0))
zaalLijst.append(Zaal("C0.110", 117, 0, 0))
zaalLijst.append(Zaal("C1.112", 60, 0, 0))
