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

    # maak een populatie zo groot als voorgeschreven
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
            print("id ouder 1: " +str(len(activiteitenIdsOuder1)))
            print("activiteiten ouder 1: " +str(len(activiteitenOuder1)))

            activiteitenOuder2 = []
            activiteitenIdsOuder2 = []

            # kies de activiteiten van ouder 2 die niet door ouder 1 zijn toegevoegd
            for activiteit in ouder2.activiteitenLijst:
                if activiteit.activiteitId not in activiteitenIdsOuder1:
                    activiteitenOuder2.append(activiteit)
                    activiteitenIdsOuder2.append(activiteit.activiteitId)

            print("id ouder 2: " +str(len(activiteitenIdsOuder2)))
            print("activiteiten ouder 2: " +str(len(activiteitenOuder2)))

            zaalslotenOuder1 = []
            zaalslotenOuder2 = []
            vrijeZaalslotenOuder1 = []
            zaalslotenKind = []
            NogInTeRoosteren = []

            # zoek in ouder1 naar de zaalsloten van de juist activiteiten en sla alle vrije zaalsloten op
            for zaalslot in ouder1.zaalslotenLijst:
                if zaalslot.activiteit == None:
                    vrijeZaalslotenOuder1.append(zaalslot.zaalslotId)
                    continue
                elif zaalslot.activiteit.activiteitId in activiteitenIdsOuder1:
                    zaalslotenOuder1.append(zaalslot)

            # voeg de zaalsloten van de ouder toe aan het kind
            for zaalslot in zaalslotenOuder1:
                zaalslotenKind.append(zaalslot)

            print("zaalsloten ouder 1: " +str(len(zaalslotenOuder1)))

            # zoek de zaalsloten bij de gekozen activiteiten van ouder2
            for zaalslot in ouder2.zaalslotenLijst:
                if zaalslot.activiteit == None:
                    continue
                elif zaalslot.activiteit.activiteitId in activiteitenIdsOuder2:
                    zaalslotenOuder2.append(zaalslot)

            print("zaalsloten ouder 2: " +str(len(zaalslotenOuder2)))

            # kijk of de zaalsloten van ouder 2 bij het kind kunnen worden toegevoegd, anders in aparte array zetten
            for zaalslot in zaalslotenOuder2:
                if zaalslot.zaalslotId in vrijeZaalslotenOuder1:
                    zaalslotenKind.append(zaalslot)
                else:
                    NogInTeRoosteren.append(zaalslot.activiteit)

            zaalslotenKindIds = []

            # zoek alle zaalsloten van het kind op
            for zaalslot in zaalslotenKind:
                zaalslotenKindIds.append(zaalslot.zaalslotId)
            print(len(ouder1.activiteitenLijst))
            print("nog in te roosteren" + str(len(NogInTeRoosteren)))
            print(" ingeroosterd" + str(len(zaalslotenKind)))

            vrijeZaalslotenKind = []

            # zaalsloten vinden die nog leeg zijn
            for zaalslot in ouder1.zaalslotenLijst:
                if zaalslot.zaalslotId not in zaalslotenKindIds:
                    vrijeZaalslotenKind.append(zaalslot)

            print("vrije zaalsloten kind: " + str(len(vrijeZaalslotenKind)))

            # voeg vrije activiteien toe aan vrij zaalsloten, nu nog random!
            for i in range(len(NogInTeRoosteren)):
                vrijeZaalslotenKind[i].voegToe(NogInTeRoosteren[i])

            # voeg de laatste ingeroosterde zaalsloten toe aan de zaalslotenlijst van het kind
            zaalslotenKind.extend(vrijeZaalslotenKind)

            # verzamel alle activiteiten en voeg ze toe aan een lijst voor het kinderen
            activiteitenKind = []
            for zaalslot in zaalslotenKind:
                activiteitenKind.append(zaalslot.activiteit)

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
