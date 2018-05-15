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



    minIteraties = 100
    score = rooster.score()

    mutaties = 0
    lijstScore = []

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
            # print(score)

        else:
            randomZaalslot2.wissel(randomZaalslot1)

        print("Score 1: " + str(score))
        print("score 2: " + str(score2))

    return [rooster, rooster.score()]

    # nu een hillcliber of iets om dit vakspreiding te minimaliseren
    # dan studenten wisselen tussen vakken om te kijken of je nog kan verbeteren > opletten dat je dan studenten bij beide werkcolleges wisselt
