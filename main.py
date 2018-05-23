"""
Hoofd bestand om een rooster object aan te maken en algoritmes te testen.

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

import os, sys
import csv
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "Code"))
sys.path.append(os.path.join(directory, "Code", "Classes"))
sys.path.append(os.path.join(directory, "Resultaten", "Visualisatie"))
sys.path.append(os.path.join(directory, "Code", "Algoritmes"))


from hillClimber import hillClimber
from hillClimber2 import hillClimber2
from simulatedAnnealing import simulatedAnnealing
from test2 import test2
from simulatedAnnealing import simulatedAnnealing, lineairFunctie, exponentieelFunctie, sigmoidalFunctie
from sequential import sequential
from geneticAlgorithm import geneticAlgorithm
import rooster as Rooster
from frequentieHistogram import frequentieHistogram
from iteratieVisualisatie import iteratieVisualisatie
from randomSteekproef import randomSteekproef
# from visualiseer import visualiseer

# Dagen en tijdsloten welke geldig zijn voor het rooster
dagen = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag"]
tijdsloten = ["9.00-11.00", "11.00-13.00", "13.00-15.00", "15.00-17.00", "17.00-19.00"]

# roosterEnScore = hillClimber(dagen, tijdsloten)
# rooster = roosterEnScore[0]
# score = roosterEnScore[1]
minIteraties = 100
rooster = Rooster.Rooster(dagen, tijdsloten)
rooster.vulRandom()

#randomSteekproef(rooster, 20000)

simulatedAnnealing(rooster, minIteraties, 100, 1, sigmoidalFunctie)

#
# rooster, scoreLijst = hillClimber2(rooster, minIteraties)
# iteratieVisualisatie(scoreLijst)

scoreLijst = []
iteraties = 1
for i in range(iteraties):
    rooster = Rooster.Rooster(dagen, tijdsloten)
    rooster.vulRandom()
    nieuwRooster = geneticAlgorithm(rooster, dagen, tijdsloten, 50, 100, 0.75)
    scoreLijst.append(nieuwRooster[0].score())
    print("we zijn bij interatie: " + str(i))

# #Assuming res is a flat list
# with open("resultaat.csv", "w") as output:
#     writer = csv.writer(output, lineterminator='\n')
#     for val in nieuwRooster[1]:
#         writer.writerow([val])
#sequential(dagen, tijdsloten)

# groottePopulatie = 10
# aantalGeneraties = 5
# hoi = geneticAlgorithm(rooster, dagen, tijdsloten, groottePopulatie, aantalGeneraties)
#
# hoi.scoreOnderverdeeld()


# rooster = roosterEnScore[0]
# score = roosterEnScore[1]
# visualiseer(tijdsloten, dagen, rooster)

# maak een random steekproef aan van x iteraties
# iteraties = 51
# randomSteekproef(rooster, 20000)

print("WELKOM BIJ HET INPLANNEN VAN DE LESROOSTERS")
def uitvoer():
    algoritme = input("Welke algoritme wil je uitproberen? \nJe kunt kiezen uit hillClimber, hillClimber2, simulatedAnnealing, sequential of geneticAlgorithm\n")
    aantalIteraties = input("Met hoeveel iteraties wil je dit algoritme uitvoeren?\n")
    print("Cool, laten we " + algoritme + " met " + aantalIteraties +" iteraties uitvoeren!")

    if algoritme == "hillClimber":
        roosterNieuw, scoreNieuw = hillClimber(rooster, int(aantalIteraties))
        print(roosterNieuw, scoreNieuw)
    if algoritme == "hillClimber2":
        roosterNieuw, scoreNieuw = hillClimber2(rooster, int(aantalIteraties))
        print(roosterNieuw, scoreNieuw)
    if algoritme == "simulatedAnnealing":
        roosterNieuw = (simulatedAnnealing(dagen, tijdsloten))[0]
        scoreNieuw = (simulatedAnnealing(dagen, tijdsloten))[1]

    nogEenKeer = input("Wil je nog een algoritme op dit rooster uitproberen? (j/n)\n")
    if nogEenKeer == "j":
        return uitvoer()
    else:
        print("Bedankt! Hopelijk ben je tevreden met je rooster.")
uitvoer()

# scoreLijst = []
# iteraties = 100
# for i in range(iteraties):
#     rooster = Rooster.Rooster(dagen, tijdsloten)
#     rooster.vulRandom()
#     nieuwRooster = simulatedAnnealing(rooster, 1500)
#     scoreLijst.append(nieuwRooster.score())
#     print(i)
#
# frequentieHistogram(scoreLijst)
