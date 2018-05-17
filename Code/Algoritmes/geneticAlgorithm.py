"""
Algoritme dat een rooster zoekt door recombinatie en mutatie.

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

import random
import rooster as Rooster
from operator import itemgetter

def geneticAlgorithm(dagen, tijdsloten, groottePopulatie, aantalGeneraties):

    # creëer populatie bestaande uit willekeurige roosters
    populatie = []

    for i in range(groottePopulatie):
        burger = Rooster.Rooster(dagen, tijdsloten)
        burger.vulRandom()
        populatie.append([burger, burger.score()])


    # iteraar door bepaald aantal generaties
    for i in range(aantalGeneraties):
        # maak generatie van kinderen ter grootte van de populatie
        kinderen = []
        for kind in range(groottePopulatie):

            # selecteer willekeurig twee ouders uit de populatie
            oudersIndex = random.sample(range(groottePopulatie), 2)
            ouder1 = (populatie[oudersIndex[0]])[0]
            ouder2 = (populatie[oudersIndex[1]])[0]


            kind = Rooster.Rooster(dagen, tijdsloten)

            ######################### RECOMBINATIE
            # recombineer ouders door van ieder willekeurige, halve aantal activiteiten te gebruiken
            aantalActiviteiten = len(ouder1.activiteitenLijst)

            # kies de indeces helft van de activiteiten van ouder 1
            indexActiviteiten = random.sample(range(aantalActiviteiten), round(aantalActiviteiten/2))

            activiteitenOuder1 = []
            activiteitenIdsOuder1 = []

            # selecter de gekozen eerste helft van activiteiten van ouder 1
            for i in range(len(indexActiviteiten)):
                activiteit = ouder1.activiteitenLijst[indexActiviteiten[i]]
                activiteitenOuder1.append(activiteit)
                activiteitenIdsOuder1.append(activiteit.activiteitId)


            activiteitenOuder2 = []
            activiteitenIdsOuder2 = []

            # kies de activiteiten van ouder 2 die niet door ouder 1 zijn toegevoegd
            for activiteit in ouder2.activiteitenLijst:
                if activiteit.activiteitId not in activiteitenIdsOuder1:
                    activiteitenOuder2.append(activiteit)
                    activiteitenIdsOuder2.append(activiteit.activiteitId)

            activiteitenKind = []
            zaalslotenKind = []
            legeZaalslotenOuder1 = []
            legeZaalslotenId = []

            # zoek de juiste zaalsloten bij de activiteiten van ouder 1, voeg deze zaalsloten toe aan de zaalsloten kind
            for zaalslot in ouder1.zaalslotenLijst:
                if zaalslot.activiteit == None:
                    legeZaalslotenOuder1.append(zaalslot)
                    legeZaalslotenId.append(zaalslot.zaalslotId)
                elif zaalslot.activiteit.activiteitId in activiteitenIdsOuder1:
                    zaalslotenKind.append(zaalslot)
                    activiteitenKind.append(activiteit)

            # voeg activiteiten van ouder 2 toe
            inTeRoosteren = []

            for zaalslot in ouder2.zaalslotenLijst


            for activiteit in activiteitenOuder2:
                # rooster zaalslot wanneer deze leeg is
                for zaalslot in ouder2.zaalslotenLijst:
                    if zaalslot.zaalslotId in legeZaalslotenId:
                        zaalslotenKind.append(zaalslot)
                        activiteitenKind.append(activiteit)
                        legeZaalslotenId.remove(zaalslot.zaalslotId)
                    # hou bij welke activiteiten nog ingeroosterd moeten worden
                    else:
                        inTeRoosteren.append(activiteit)
