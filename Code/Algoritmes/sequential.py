import random

def sequential(rooster):

    # plaats de activiteiten in beschikbaar slot, aan de hand van score (zaalgrote/grootte groep)

    # maak een random volgorde van de activiteitenlijst
    random.shuffle(rooster.zaalslotenLijst, random.random)

    # sorteer de activiteiten op het aantal studenten per activiteit
    rooster.activiteitenLijst.sort(key = lambda x: x.nrStud, reverse = True)

    # sorteer de zaalsloten op het aantal studenten per activiteit
    rooster.zaalslotenLijst.sort(key = lambda x: x.capaciteit, reverse = True)

    j = 0
    # voeg de activiteiten toe aan de zaalsloten, sla de zaalsloten van 17.00-19.00 over
    for i in range(len(rooster.activiteitenLijst)):
        while(rooster.zaalslotenLijst[j].tijdslot == 5):
            j += 1

        rooster.zaalslotenLijst[j].voegToe(rooster.activiteitenLijst[i])
        j += 1


    # nu een hillcliber of iets om dit vakspreiding te minimaliseren
    # dan studenten wisselen tussen vakken om te kijken of je nog kan verbeteren > opletten dat je dan studenten bij beide werkcolleges wisselt



def sequentialRandom(rooster):
    "Vult het rooster met activiteiten"


    acceptatie = 0.8

    # maak een random volgorde van de activiteitenlijst
    random.shuffle(rooster.activiteitenLijst, random.random)

    for activiteit in rooster.activiteitenLijst:
        while(True):
            zaalslot = random.choice(rooster.zaalslotenLijst)
            if (activiteit.nrStud / zaalslot.capaciteit) > acceptatie and (activiteit.nrStud / zaalslot.capaciteit) <= acceptatie and zaalslot.inGebruik == 0:
                zaalslot.voegToe(activiteit)
                break
