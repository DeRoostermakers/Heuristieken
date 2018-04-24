"""
Bestand met functie die de maluspunten voor studenten die niet in de zaal passen berekent

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

rooster = {"maandag": {"slot1": [3, 1], "slot2": [4, 5]}, "dinsdag": {"slot1": [3, 1], "slot2": [4, 5]}}

week = rooster.keys()

for dag in week: 
    tijdsloten = rooster[dag].keys()
    
    for tijdslot in tijdsloten:
        zalen =rooster[dag][tijdslot]
        
        for zaal in zalen:
            print(zaal)
    
        

def zaalgrootteConflict():
    "deze functie berekent de maluspunten voor te kleine zalen"
    
    malusPunten = 0
        
    return malusPunten