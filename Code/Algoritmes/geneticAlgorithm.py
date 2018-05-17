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

            for zaalslot in ouder1.zaalslotenLijst:
                if zaalslot.activiteit == None:
                    vrijeZaalslotenOuder1.append(zaalslot.zaalslotId)
                    continue
                elif zaalslot.activiteit.activiteitId in activiteitenIdsOuder1:
                    zaalslotenOuder1.append(zaalslot)

            for zaalslot in zaalslotenOuder1:
                zaalslotenKind.append(zaalslot)

            print("zaalsloten ouder 1: " +str(len(zaalslotenOuder1)))

            for zaalslot in ouder2.zaalslotenLijst:
                if zaalslot.activiteit == None:
                    continue
                elif zaalslot.activiteit.activiteitId in activiteitenIdsOuder2:
                    zaalslotenOuder2.append(zaalslot)

            print("zaalsloten ouder 2: " +str(len(zaalslotenOuder2)))

            for zaalslot in zaalslotenOuder2:
                if zaalslot.zaalslotId in vrijeZaalslotenOuder1:
                    zaalslotenKind.append(zaalslot)
                else:
                    NogInTeRoosteren.append(zaalslot.activiteit)

            zaalslotenKindIds = []
            for zaalslot in zaalslotenKind:
                zaalslotenKindIds.append(zaalslot.)
            print(len(ouder1.activiteitenLijst))
            print("nog in te roosteren" + str(len(NogInTeRoosteren)))
            print(" ingeroosterd" + str(len(zaalslotenKind)))

            # zaalsloten vinden die nog leeg zijn
            for zaalslot in ouder1.zaalslotenLijst:




            # activiteitenKind = []
            # zaalslotenKind = []
            # legeZaalslotenOuder1 = []
            # legeZaalslotenId = []
            #
            # # zoek de juiste zaalsloten bij de activiteiten van ouder 1, voeg deze zaalsloten toe aan de zaalsloten kind
            # for zaalslot in ouder1.zaalslotenLijst:
            #     if zaalslot.activiteit == None:
            #         legeZaalslotenOuder1.append(zaalslot)
            #         legeZaalslotenId.append(zaalslot.zaalslotId)
            #     elif zaalslot.activiteit.activiteitId in activiteitenIdsOuder1:
            #         zaalslotenKind.append(zaalslot)
            #         activiteitenKind.append(zaalslot.activiteit)
            #     else:
            #         legeZaalslotenId.append(zaalslot.zaalslotId)
            #
            # print(zaalslotenKind)
            # print(legeZaalslotenId)
            # print(activiteitenKind)
            #
            # # voeg activiteiten van ouder 2 toe aan de zaalsloten van het kind, als deze vrij zijn, ander bewaar ze
            # inTeRoosteren = []
            #
            # for zaalslot in ouder2.zaalslotenLijst:
            #     if zaalslot.activiteit == None:
            #         continue
            #     elif zaalslot.activiteit.activiteitId in activiteitenIdsOuder2 and zaalslot.zaalslotId not in legeZaalslotenId:
            #         inTeRoosteren.append(activiteit)
            #     elif zaalslot.activiteit.activiteitId in activiteitenIdsOuder2 and zaalslot.zaalslotId in legeZaalslotenId:
            #         zaalslotenKind.append(zaalslot)
            #         activiteitenKind.append(zaalslot.activiteit)
            #         legeZaalslotenId.remove(zaalslot.zaalslotId)
            #
            # print(inTeRoosteren)
            #
            # for activiteit in inTeRoosteren:
            #     for zaalslot in ouder1.zaalslotenLijst:
            #         if zaalslot.zaalslotId in legeZaalslotenId:
            #             zaalslot.voegToe(activiteit)
            #             legeZaalslotenId.remove(zaalslot.zaalslotId)
            #             zaalslotenKind.append(zaalslot)
            #             activiteitenKind.append(activiteit)
