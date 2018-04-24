"""
Bestand met functie die de maluspunten voor studenten die niet in de zaal passen berekent

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""     

def zaalgrootteConflict(zaalslotLijst):
    "deze functie berekent de maluspunten voor te kleine zalen"
    
    malusPunten = 0
    
    for zaalslot in zaalslotLijst:
        verschil = zaalslot.capaciteit - zaalslot.activiteit.nrStud
        if verschil < 0:
            malusPunten = malusPunten + abs(verschil)
        
    return malusPunten