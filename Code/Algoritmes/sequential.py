import random
import rooster as Rooster
import math

def sequential(dagen, tijdsloten):
    legeVakken = []

    rooster = Rooster.Rooster(dagen, tijdsloten)

    # maak een random volgorde van de zaalslotenlijst
    random.shuffle(rooster.zaalslotenLijst, random.random)

    # maak een random volgorde van de activiteitenlijst
    random.shuffle(rooster.activiteitenLijst, random.random)

    # sorteer de activiteiten op het aantal studenten per activiteit
    rooster.activiteitenLijst.sort(key = lambda x: x.nrStud, reverse = True)

    # sorteer de zaalsloten op het aantal studenten per capaciteit
    rooster.zaalslotenLijst.sort(key = lambda x: x.capaciteit, reverse = True)

    print(len(rooster.activiteitenLijst))

    j = 0
    # voeg de activiteiten toe aan de zaalsloten, sla de zaalsloten van 17.00-19.00 over
    for i in range(len(rooster.activiteitenLijst)):
        if(rooster.activiteitenLijst[i].nrStud == 0):
            legeVakken.append(rooster.activiteitenLijst[i])
            continue

        while(rooster.zaalslotenLijst[j].tijdslot == 5):
            j += 1

        rooster.zaalslotenLijst[j].voegToe(rooster.activiteitenLijst[i])
        j += 1

    k = 0
    for zaalslot in rooster.zaalslotenLijst:
        if zaalslot.inGebruik == 0:
            zaalslot.voegToe(legeVakken[k])
            k += 1

    print(legeVakken)

    print("score na sequential stap 1: " + str(rooster.score()))

    # zalen = [[]  for i in range(len(rooster.zaalNaarID))]
    # for zaalslot in rooster.zaalslotenLijst:
    #     zalen[rooster.zaalNaarID[zaalslot.naam]].append(zaalslot)

    # for zaal in zalen:
    #     scoreOud = rooster.score()
    #     for i in range(50):
    #         # wissel twee willekeurige zaalsloten
    #         indexZaalslot = random.sample(range(len(zaal)), 2)
    #         randomZaalslot1 = zaal[indexZaalslot[0]]
    #         randomZaalslot2 = zaal[indexZaalslot[1]]
    #         randomZaalslot1.wissel(randomZaalslot2)
    #         scoreNieuw = rooster.score()
    #         if scoreNieuw > scoreOud:
    #             scoreOud = scoreNieuw
    #         else:
    #             randomZaalslot2.wissel(randomZaalslot1)
    #
    # return [rooster, rooster.score()]

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


    print(rooster.score())

    beginTemperatuur = 100
    eindTemperatuur = 0
    minIteraties = 2000
    score = rooster.score()
    mutaties = 0
    lijstScore = []
    simulatedAnnelingRooster = []
    for i in range(minIteraties):

        # wissel twee willekeurige zaalsloten
        indexZaalslot = random.sample(range(len(rooster.zaalslotenLijst)), 2)
        randomZaalslot1 = rooster.zaalslotenLijst[indexZaalslot[0]]
        randomZaalslot2 = rooster.zaalslotenLijst[indexZaalslot[1]]
        randomZaalslot1.wissel(randomZaalslot2)
        score2 = rooster.score()
        lijstScore.append(score)

        if score2 > score:
            score = score2
            mutaties += 1

        else:
            # nog steeds geaccepteerd toegestaan
            temperatuur = beginTemperatuur-i*(beginTemperatuur-eindTemperatuur)/minIteraties
            verkorting = score2 - score
            acceptatieKans = math.exp(verkorting/temperatuur)
            # print(acceptatieKans)

            nummer = random.random()
            if acceptatieKans > nummer:
                score = score2
                mutaties += 1

            # niet geaccepteerd
            randomZaalslot2.wissel(randomZaalslot1)

    simulatedAnnelingRooster.append([rooster, score])

    aantalIteraties = []
    for i in range(minIteraties):
        aantalIteraties.append(i)

    # print(aantalIteraties)
    print(lijstScore)


def sequentialTres(dagen, tijdsloten):

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

    zalenTemp = [[]  for i in range(len(rooster.zaalNaarID))]
    for zaalslot in rooster.zaalslotenLijst:
        zalenTemp[rooster.zaalNaarID[zaalslot.naam]].append(zaalslot)

    zalen = [[] for i in range(4)]
    zalen[0].extend(zalenTemp[0])
    zalen[1].extend(zalenTemp[1])
    zalen[1].extend(zalenTemp[2])
    zalen[2].extend(zalenTemp[3])
    zalen[0].extend(zalenTemp[4])
    zalen[3].extend(zalenTemp[5])
    zalen[2].extend(zalenTemp[6])
    print(zalen)
    print("score na sequential stap 1: " + str(rooster.score()))


    lijstScore = []
    simulatedAnnelingRooster = []
    for zaal in zalen:
        beginTemperatuur = 100
        eindTemperatuur = 0
        minIteraties = 1000
        score = rooster.score()
        mutaties = 0

        for i in range(minIteraties):
            # wissel twee willekeurige zaalsloten
            indexZaalslot = random.sample(range(len(rooster.zaalslotenLijst)), 2)
            randomZaalslot1 = rooster.zaalslotenLijst[indexZaalslot[0]]
            randomZaalslot2 = rooster.zaalslotenLijst[indexZaalslot[1]]
            randomZaalslot1.wissel(randomZaalslot2)
            score2 = rooster.score()
            lijstScore.append(score)

            if score2 > score:
                score = score2
                mutaties += 1

            else:
                # nog steeds geaccepteerd toegestaan
                temperatuur = beginTemperatuur-i*(beginTemperatuur-eindTemperatuur)/minIteraties
                verkorting = score2 - score
                acceptatieKans = math.exp(verkorting/temperatuur)
                # print(acceptatieKans)

                nummer = random.random()
                if acceptatieKans > nummer:
                    score = score2
                    mutaties += 1

                # niet geaccepteerd
                randomZaalslot2.wissel(randomZaalslot1)

        simulatedAnnelingRooster.append([rooster, score])

        aantalIteraties = []
        for i in range(minIteraties):
            aantalIteraties.append(i)

    # print(aantalIteraties)
    print(lijstScore)
    print(len(lijstScore))
    return [rooster, rooster.score()]
