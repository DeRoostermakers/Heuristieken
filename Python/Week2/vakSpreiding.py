
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
                    verdeeldAantalDagen = verdeeldAantalDagen + 1                    
                            
        aantalActiviteiten = vak.hc + vak.wc + vak.prac
        
        
                            
                            
                            
                            
                            


