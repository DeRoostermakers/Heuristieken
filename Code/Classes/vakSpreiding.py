"""
Bestand met functie die de maluspunten voor de vakspreiding berekent

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

def vakSpreiding(vakkenLijst, activiteitenLijst):
    "deze functie berekent de punten voor de spreiding van de activiteiten"
    
    malusPunten = 0
    
    for vak in vakkenLijst:
        verdeeldAantalDagen = 0
        dag = []
        for activiteit in activiteitenLijst:
            if activiteit.vakId == vak.id:
                if activiteit.dag not in dag:
                    dag.append(activiteit.dag)
                    verdeeldAantalDagen =+ 1                    
                            
        aantalActiviteiten = vak.hc + vak.wc + vak.prac
        
        x = aantalActiviteiten - verdeeldAantalDagen
        
        malusPunten = malusPunten + x * 10
        
    return malusPunten