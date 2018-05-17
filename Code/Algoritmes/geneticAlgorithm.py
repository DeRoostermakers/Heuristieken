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
        nieuwRooster = Rooster.Rooster(dagen, tijdsloten)
        nieuwRooster.vulRandom()
        burger = [nieuwRooster]
        burger.append(nieuwRooster.score())
        populatie.append(burger)

    # itereer door bepaald aantal generaties
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
            activiteitenOuder2 = []

            # selecter de gekozen eerste helft van activiteiten van ouder 1
            for i in range(len(indexActiviteiten)):
                activiteit = ouder1.activiteitenLijst[indexActiviteiten[i]]
                activiteitenOuder1.append(activiteit)
                activiteitenIdsOuder1.extend(activiteit.activiteitId)

            # kies de activiteiten van ouder 2 die niet door ouder 1 zijn toegevoegd
            for activiteit in ouder2.activiteitenLijst:
                if activiteit.activiteitId not in activiteitenIdsOuder1:
                    activiteitenOuder2.append(activiteit)

            activiteitenKind = []
            zaalslotenKind = []
            legeZaalslotenOuder1 = []
            legeZaalslotenId = []

            # zoek de juiste zaalsloten bij de activiteit van ouder 1
            for activiteit in activiteitenOuder1:
                for zaalslot in ouder1.zaalslotenLijst:
                    if zaalslot.activiteit == None:

                        # controleren dat je niet elke ronde steeds de lege zaalsloten toevoegd
                        if zaalslot not in legeZaalslotenOuder1:
                            legeZaalslotenOuder1.append(zaalslot)
                        if zaalslot.zaalslotId not in legeZaalslotenId:
                            legeZaalslotenId.append(zaalslot.zaalslotId)

                    # voeg zaalslot van activiteit van ouder 1 aan kind toe
                    elif zaalslot.activiteit.activiteitId == activiteit.activiteitId:
                        zaalslotenKind.append(zaalslot)

            # voeg activiteiten van ouder 2 toe
            inTeRoosteren = []
            for activiteit in activiteitenOuder2:

                # rooster zaalslot wanneer deze leeg is
                for zaalslot in ouder2.zaalslotenLijst:
                    if zaalslot.zaalslotId in legeZaalslotenId:
                        zaalslotenKind.append(zaalslot)

                        # verwijder zaalslot uit lege lijst als hij in gebruik is
                        for slot in legeZaalslotenId:
                            if slot == zaalslot.zaalslotId:
                                legeZaalslotenId.remove(slot)

                    # hou bij welke activiteiten nog ingeroosterd moeten worden
                    else:
                        inTeRoosteren.append(activiteit)

            # rooster overgebleven activiteiten in
            i = 0
            for activiteit in inTeRoosteren:
                for zaalslot in legeZaalslotenOuder1:
                    if zaalslot.zaalslotId not in legeZaalslotenId:
                        zaalslot.voegToe(activiteit)
                        zaalslotenKind.append(zaalslot)

            print(activiteitenKind)
            kind.activiteitenLijst = activiteitenKind
            kind.zaalslotenLijst = zaalslotenKind

            # muteer kind met 10% kans
            een = 1
            nummer = random.sample(range(10), een)
            if een in nummer:

                # wissel twee willekeurige zaalsloten
                indexZaalslot = random.sample(range(len(kind.zaalslotenLijst)), 2)
                randomZaalslot1 = kind.zaalslotenLijst[indexZaalslot[0]]
                randomZaalslot2 = kind.zaalslotenLijst[indexZaalslot[1]]
                randomZaalslot1.wissel(randomZaalslot2)

            i = 0
            for zaalslot in kind.zaalslotenLijst:
                # print(zaalslot)
                i += 1
            print(i)

            # voeg kind toe aan generatie van kinderen
            kinderen.append([kind, kind.score()])

        # sorteer totale populatie op scores
        totalePopulatie = kinderen + populatie
        populatieGesorteerd = sorted(totalePopulatie, key=itemgetter(1), reverse = True)

        # selecteer beste 50 roosters uit de populatie
        populatie = populatieGesorteerd[:groottePopulatie]

    # selecteer beste rooster van laatste populatie
    populatieGesorteerd = sorted(populatie, key=itemgetter(1))
    besteScore = populatieGesorteerd[0]

    return besteScore
