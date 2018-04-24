"""
Bestand met functie die de score van een geldig rooster berekent

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

def scoreFunctie(vakkenLijst, activiteitenLijst, zaalslotLijst, studentenLijst):
    "deze functie berekent de score van een rooster"
    malusPunten = vakSpreiding(vakkenLijst, activiteitenLijst) + zaalgrootteConflict(zaalslotLijst) + roosterConflicten(studentenLijst, zaalslotLijst) + extraTijdslot(studentenLijst, zaalslotLijst)
    score = 1000 - malusPunten
