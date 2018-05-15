"""
Algoritme dat een rooster zoekt door recombinatie en mutatie.

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

import random
from operator import itemgetter

def geneticAlgorithm(rooster, groottePopulatie, aantalGeneraties):
    
    # creëer populatie bestaande uit willekeurige roosters
    populatie = []
    for i in range(groottePopulatie):
        burger = [rooster.vulRandom()]
        burger.extend(burger.score())
        populatie.append(burger)
    
    # iteraar door bepaald aantal generaties
    for i in range(aantalGeneraties):
        
        # maak generatie van kinderen ter grootte van de populatie
        kinderen = []
        for kind in range(groottePopulatie):
            
            # selecteer willekeurig twee ouders uit de populatie
            oudersIndex = random.sample(range(groottePopulatie), 2)
            ouder1 = (populatie(oudersIndex[0]))[0]
            ouder2 = (populatie(oudersIndex[1]))[0]
            kind = rooster
            
            ######################### RECOMBINATIE
            # recombineer ouders door van ieder helft van activiteiten te gebruiken
            # aantalActiviteiten = len(ouder1.activiteitenLijst)
            # indexActiviteiten = random.sample(range(aantalActiviteiten), aantalActiviteiten/2)
        
            # plaatst helft van de activiteiten van ouder1 in zaalsloten van kind
            i = 0
            j = 0
            for zaalslot in range(0, len(ouder2.activiteitenLijst)):
                kind.zaalslotenLijst[j].voegToe(kind.activiteitenLijst[i])
                i += 1
                j += 1
            ######################### RECOMBINATIE
            
            # muteer kind met 10% kans
            een = 1
            nummer = random.sample(range(10), een)
            if een in nummer:
                
                # wissel twee willekeurige zaalsloten
                indexZaalslot = random.sample(range(len(kind.zaalslotenLijst)), 2)
                randomZaalslot1 = kind.zaalslotenLijst(indexZaalslot[0])
                randomZaalslot2 = kind.zaalslotenLijst(indexZaalslot[1])
                randomZaalslot1.wissel(randomZaalslot2)
                
            # voeg kind toe aan generatie van kinderen
            kinderen.append([kind, kind.score()])
        
        # sorteer kinderen en ouders van laagste naar hoogste score
        kinderenGesorteerd = sorted(kinderen, key=itemgetter(1))
        oudersGesorteerd = sorted(populatie, key=itemgetter(1))
        
        ####################### KLOPT VOLGENS MIJ NOG NIET
        # selecteer de beste scores van ouders en kinderen
        j = 0
        score = 1
        for kind in kinderenGesorteerd:
            if kind[score] >= oudersGesorteerd[0][score]:
                oudersGesorteerd.pop(j)
                oudersGesorteerd == [kind] + oudersGesorteerd
            if kind[score] < oudersGesorteerd[0][score]: 
                j += 1
        
        # herhaal proces voor nieuwe populatie
        populatie = oudersGesorteerd
    
    # selecteer beste rooster van laatste populatie
    populatieGesorteerd = sorted(populatie, key=itemgetter(1))
    besteRooster = populatieGesorteerd[0][0]
    
    return besteRooster