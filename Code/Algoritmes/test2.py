"""
Algoritme dat een rooster zoekt door recombinatie en mutatie.

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

import random
import rooster as Rooster
import copy
from operator import itemgetter
from willekeurigeWissel import willekeurigeWissel

# hoeveel activiteiten van rooster 1, hoeveel activiteiten van ouder 2
# op welke manier worden de laatste nog in te roosteren activiteiten ingeroosterd
# kijken of het nog mooier geschreven kan worden

def test2(rooster, dagen, tijdsloten, groottePopulatie, aantalGeneraties, mutatieKans):

    scoreLijst = []
    # creëer populatie bestaande uit willekeurige roosters
    populatie = maakPopulatie(rooster, dagen, tijdsloten, groottePopulatie)

    # iteraar door bepaald aantal generaties
    for j in range(aantalGeneraties):
        # maak generatie van kinderen ter grootte van de populatie
        kinderen = []
        for kind in range(groottePopulatie):

            ouder1, ouder2 = kiesOuders(populatie, groottePopulatie)

            kind = Rooster.Rooster(dagen, tijdsloten)

            # maak een kind rooster uit de twee ouders
            recombinatie(ouder1, ouder2, kind)

            # muteer kind rooster met een mogelijke kans
            mutatie(kind.zaalslotenLijst, mutatieKans)

            # voeg kind toe aan generatie van kinderen
            kinderen.append([kind, kind.score()])

        # sorteer totale populatie op scores
        totalePopulatie = kinderen + populatie
        populatieGesorteerd = sorted(totalePopulatie, key=itemgetter(1), reverse = True)

        # selecteer beste 50 roosters uit de populatie
        populatie = populatieGesorteerd[:groottePopulatie]
        scoreLijst.append(populatieGesorteerd[0][0].score())
        print("generatie " + str(j))

    return [populatieGesorteerd[0][0], scoreLijst]

def kiesOuders(populatie, groottePopulatie):
    # selecteer willekeurig twee ouders uit de populatie
    oudersIndex = random.sample(range(groottePopulatie), 2)
    ouder1 = (populatie[oudersIndex[0]])[0]
    ouder2 = (populatie[oudersIndex[1]])[0]

    return ouder1, ouder2


def maakPopulatie(rooster, dagen, tijdsloten, groottePopulatie):
    # creëer populatie bestaande uit willekeurige roosters
    populatie = []

    # voeg het meegegeven rooster toe aan de populatie
    populatie.append([rooster, rooster.score()])

    # maak een populatie zo groot als voorgeschreven
    for i in range(groottePopulatie - 1):
        burger = Rooster.Rooster(dagen, tijdsloten)
        burger.vulRandom()
        populatie.append([burger, burger.score()])

    return populatie

def recombinatie(ouder1, ouder2, kind):
    # recombineer ouders door van iedere ouder willekeurig aantal activiteiten te nemen
    aantalActiviteiten = len(ouder1.activiteitenLijst)

    # kies de activiteiten van ouder 1
    indexActiviteiten = random.sample(range(aantalActiviteiten), random.randint(0,aantalActiviteiten))

    activiteitenOuder1 = []
    activiteitenIdsOuder1 = []

    # selecter de gekozen activiteiten van ouder 1
    for i in range(len(indexActiviteiten)):
        activiteit = ouder1.activiteitenLijst[indexActiviteiten[i]]
        # sla lege activiteiten over
        if activiteit.nrStud == 0:
            continue
        else:
            activiteitenOuder1.append(activiteit)
            activiteitenIdsOuder1.append(activiteit.activiteitId)

    activiteitenOuder2 = []
    activiteitenIdsOuder2 = []

    # kies de activiteiten van ouder 2 die niet door ouder 1 zijn toegevoegd
    for activiteit in ouder2.activiteitenLijst:
        if activiteit.activiteitId not in activiteitenIdsOuder1:
            activiteitenOuder2.append(activiteit)
            activiteitenIdsOuder2.append(activiteit.activiteitId)

    zaalslotenOuder1 = []
    zaalslotenOuder2 = []
    zaalslotenIdOuder1 = []
    zaalslotenKind = []
    NogInTeRoosteren = []

    # zoek in ouder1 naar de zaalsloten van de juist activiteiten
    for zaalslot in ouder1.zaalslotenLijst:
        if zaalslot.activiteit.activiteitId in activiteitenIdsOuder1:
            zaalslotenOuder1.append(zaalslot)
            zaalslotenIdOuder1.append(zaalslot.zaalslotId)

    # voeg de zaalsloten van de ouder toe aan het kind EXTENDEN IS SNELLER?
    for zaalslot in zaalslotenOuder1:
        zaalslotenKind.append(copy.deepcopy(zaalslot))

    # zoek de zaalsloten bij de gekozen activiteiten van ouder2
    for zaalslot in ouder2.zaalslotenLijst:
        if zaalslot.activiteit.activiteitId in activiteitenIdsOuder2:
            zaalslotenOuder2.append(zaalslot)

    # kijk of de zaalsloten van ouder 2 bij het kind kunnen worden toegevoegd, anders in aparte array zetten
    for zaalslot in zaalslotenOuder2:
        if zaalslot.zaalslotId not in zaalslotenIdOuder1:
            zaalslotenKind.append(copy.deepcopy(zaalslot))
        else:
            NogInTeRoosteren.append(copy.deepcopy(zaalslot.activiteit))

    zaalslotenKindIds = []

    # zoek alle zaalsloten van het kind op
    for zaalslot in zaalslotenKind:
        zaalslotenKindIds.append(zaalslot.zaalslotId)

    vrijeZaalslotenKind = []

    # zaalsloten vinden die nog leeg zijn
    for zaalslot in ouder1.zaalslotenLijst:
        if zaalslot.zaalslotId not in zaalslotenKindIds:
            vrijeZaalslotenKind.append(copy.deepcopy(zaalslot))

    # sorteer de activiteiten op het aantal studenten per activiteit
    NogInTeRoosteren.sort(key = lambda x: x.nrStud, reverse = True)

    # sorteer de zaalsloten op het aantal studenten per capaciteit
    vrijeZaalslotenKind.sort(key = lambda x: x.capaciteit, reverse = True)

    # voeg vrije activiteien toe aan vrij zaalsloten op zaalgrootte
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

def mutatie(zaalslotenLijst, mutatieKans):
        # muteer kind met een mutatiekans
        een = 1
        nummer = random.sample(range(int(1/mutatieKans)), een)
        if een in nummer:
            # wissel twee willekeurige zaalsloten
            randomZaalslot1, randomZaalslot2 = willekeurigeWissel(zaalslotenLijst)
            randomZaalslot1.wissel(randomZaalslot2)