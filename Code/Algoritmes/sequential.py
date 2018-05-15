import random
import rooster as Rooster

def sequential(dagen, tijdsloten):

    rooster = Rooster.Rooster(dagen, tijdsloten)


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




    minIteraties = 10
    score = rooster.score()

    nieuwRooster = rooster
    mutaties = 0
    lijstScore = []
    for i in range(minIteraties):

        # wissel twee willekeurige zaalsloten
        indexZaalslot = random.sample(range(len(nieuwRooster.zaalslotenLijst)), 2)
        randomZaalslot1 = nieuwRooster.zaalslotenLijst[indexZaalslot[0]]
        randomZaalslot2 = nieuwRooster.zaalslotenLijst[indexZaalslot[1]]
        randomZaalslot1.wissel(randomZaalslot2)
        score2 = nieuwRooster.score()
        lijstScore.append(score)

        print("score 1: " + str(score))
        print("score 2: " + str(score2))
        if score2 > score:
            rooster = nieuwRooster
            score = score2
            mutaties += 1
            # print(score)

    print(lijstScore)


    return [rooster, rooster.score()]

    # nu een hillcliber of iets om dit vakspreiding te minimaliseren
    # dan studenten wisselen tussen vakken om te kijken of je nog kan verbeteren > opletten dat je dan studenten bij beide werkcolleges wisselt
