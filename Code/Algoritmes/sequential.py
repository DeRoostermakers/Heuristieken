import random
import rooster as Rooster

def sequential(dagen, tijdsloten):

    rooster = Rooster.Rooster(dagen, tijdsloten)

    # maak een random volgorde van de zaalslotenlijst
    random.shuffle(rooster.zaalslotenLijst, random.random)

    # maak een random volgorde van de activiteitenlijst
    random.shuffle(rooster.activiteitenLijst, random.random)

    # sorteer de activiteiten op het aantal studenten per activiteit
    rooster.activiteitenLijst.sort(key = lambda x: x.nrStud, reverse = True)

    # sorteer de zaalsloten op het aantal studenten per capaciteit
    rooster.zaalslotenLijst.sort(key = lambda x: x.capaciteit, reverse = True)

    j = 0
    # voeg de activiteiten toe aan de zaalsloten, sla de zaalsloten van 17.00-19.00 over
    for i in range(len(rooster.activiteitenLijst)):
        while(rooster.zaalslotenLijst[j].tijdslot == 5):
            j += 1

        rooster.zaalslotenLijst[j].voegToe(rooster.activiteitenLijst[i])
        j += 1

    zalen = [[]  for i in range(len(rooster.zaalNaarID))]
    for zaalslot in rooster.zaalslotenLijst:
        zalen[rooster.zaalNaarID[zaalslot.naam]].append(zaalslot)

    print(zalen)
    print("score na sequential stap 1: " + str(rooster.score()))

    for zaal in zalen:
        scoreOud = rooster.score()
        for i in range(50):
            # wissel twee willekeurige zaalsloten
            indexZaalslot = random.sample(range(len(zaal)), 2)
            randomZaalslot1 = zaal[indexZaalslot[0]]
            randomZaalslot2 = zaal[indexZaalslot[1]]
            randomZaalslot1.wissel(randomZaalslot2)
            scoreNieuw = rooster.score()
            if scoreNieuw > scoreOud:
                scoreOud = scoreNieuw
            else:
                randomZaalslot2.wissel(randomZaalslot1)

    return [rooster, rooster.score()]

def sequentialDos(dagen, tijdsloten):
    rooster = Rooster.Rooster(dagen, tijdsloten)

    # maak een random volgorde van de zaalslotenlijst
    random.shuffle(rooster.zaalslotenLijst, random.random)

    # maak een random volgorde van de activiteitenlijst
    random.shuffle(rooster.activiteitenLijst, random.random)

    # sorteer de activiteiten op het aantal studenten per activiteit
    rooster.activiteitenLijst.sort(key = lambda x: x.nrStud, reverse = True)

    # sorteer de zaalsloten op het aantal studenten per capaciteit
    rooster.zaalslotenLijst.sort(key = lambda x: x.capaciteit, reverse = True)

    j = 0
    # voeg de activiteiten toe aan de zaalsloten, sla de zaalsloten van 17.00-19.00 over
    for i in range(len(rooster.activiteitenLijst)):
        while(rooster.zaalslotenLijst[j].tijdslot == 5):
            j += 1

        rooster.zaalslotenLijst[j].voegToe(rooster.activiteitenLijst[i])
        j += 1

    zalen = [[]  for i in range(len(rooster.zaalNaarID))]
    for zaalslot in rooster.zaalslotenLijst:
        zalen[rooster.zaalNaarID[zaalslot.naam]].append(zaalslot)
